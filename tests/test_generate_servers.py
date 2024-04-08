import logging
import os
import time
from os import environ
from xsdata.formats.dataclass.serializers import PycodeSerializer
from unittest import TestCase
from bs4 import BeautifulSoup
from pprint import pp
import requests
import pandas as pd

_logger = logging.getLogger(__name__)


# TODO / FIXME: not all severs provide "ConsultaCadastro".
# -> try to figure out how it works!

# TODO NFCe: https://dfe-portal.svrs.rs.gov.br/NFCE/Servicos
# TODO CTe and MDFe

class GenerateServersTest(TestCase):

    def test_generate_servers(self):
        constants = ""
        servers_list = []
        servers = {}

        prod_response = requests.get("https://www.nfe.fazenda.gov.br/portal/webServices.aspx")
        soup = BeautifulSoup(prod_response.content, 'lxml')
        captions = soup.find_all('caption')
        servers_list = []
        for caption in captions:
            if "(" not in str(caption):
                continue
            servers_list.append(str(caption).split("(")[1].split(")")[0])

        dev_response = requests.get("https://hom.nfe.fazenda.gov.br/portal/webServices.aspx")
        tables = pd.read_html(dev_response.content.decode(dev_response.apparent_encoding))
        dev_servers = {}
        for index, table in enumerate(list(tables)):
            if list(table.to_dict().keys())[0] != "Serviço":
                continue
            urls = list(dict(table.to_dict())["URL"].values())
            dev_server = urls[-1].split("/")[2]
            server = servers_list[index]
            dev_servers[server] = dev_server

        #response = requests.get("https://www.cte.fazenda.gov.br/portal/webServices.aspx?tipoConteudo=wpdBtfbTMrw=")

        tables = pd.read_html(prod_response.content.decode(prod_response.apparent_encoding))
        for index, table in enumerate(list(tables)):
            if list(table.to_dict().keys())[0] != "Serviço":
                continue
            actions = list(dict(table.to_dict())["Serviço"].values())
            urls = list(dict(table.to_dict())["URL"].values())

            if index == 0:
                for action in actions:
                    if "qrcode" in action.lower():
                        continue
                    constants += f'{action.upper()} = "{action}"\n'
            paths = ["/" + "/".join(url.split("/")[3:]) for url in urls]
            prod_server = urls[-1].split("/")[2]

            server = servers_list[index]
            action_dict = {"prod_server": prod_server, "dev_server": dev_servers[server]}
            for index, action in enumerate(actions):
                if "qrcode" in action.lower():
                    continue
                action_dict[action] = paths[index]

            servers[server] = action_dict

        print("\n")

        serializer = PycodeSerializer()
        servers = serializer.render(servers, var_name="servers")
        print(constants)
        print(servers)

