import logging
import os
import time
from os import environ
from unittest import TestCase

from decorator import decorate
from requests import Session
from requests_pkcs12 import Pkcs12Adapter

_logger = logging.getLogger(__name__)


def _only_if_valid_certificate(method, self):
    if environ.get("CERT_FILE") and environ.get("CERT_PASSWORD") and environ.get("DOWNLOAD_WSDL"):
        return method(self)
    return lambda: _logger.info(
        "Skipping test because you didn't provide a valid A1 certificate"
    )


def only_if_valid_certificate(method):
    return decorate(method, _only_if_valid_certificate)


SERVER = "https://nfe-homologacao.svrs.rs.gov.br"  # TODO should be a parameter


class DownloadWSDLTest(TestCase):
    @only_if_valid_certificate
    def test_download_wsdl_files(self):
        WSDLS = (
            # NF-e
            "https://nfe.svrs.rs.gov.br/ws/nfeinutilizacao/nfeinutilizacao4.asmx",
            "https://nfe.svrs.rs.gov.br/ws/NfeConsulta/NfeConsulta4.asmx",
            "https://nfe.svrs.rs.gov.br/ws/NfeStatusServico/NfeStatusServico4.asmx",
            "https://nfe.svrs.rs.gov.br/ws/cadconsultacadastro/cadconsultacadastro4.asmx",
            "https://nfe.svrs.rs.gov.br/ws/recepcaoevento/recepcaoevento4.asmx",
            "https://nfe.svrs.rs.gov.br/ws/NfeAutorizacao/NFeAutorizacao4.asmx",
            "https://nfe.svrs.rs.gov.br/ws/NfeRetAutorizacao/NFeRetAutorizacao4.asmx",
            "https://www1.nfe.fazenda.gov.br/NFeDistribuicaoDFe/NFeDistribuicaoDFe.asmx",

            # "https://dfe-portal.svrs.rs.gov.br/cte/qrCode",

            # CT-e
            "https://cte.svrs.rs.gov.br/ws/CTeStatusServicoV4/CTeStatusServicoV4.asmx",
            "https://cte.svrs.rs.gov.br/ws/CTeConsultaV4/CTeConsultaV4.asmx",
            "https://cte.svrs.rs.gov.br/ws/CTeRecepcaoSincV4/CTeRecepcaoSincV4.asmx",
            "https://cte.svrs.rs.gov.br/ws/CTeRecepcaoOSV4/CTeRecepcaoOSV4.asmx",
            "https://cte.svrs.rs.gov.br/ws/CTeRecepcaoGTVeV4/CTeRecepcaoGTVeV4.asmx",
            "https://cte.svrs.rs.gov.br/ws/CTeRecepcaoEventoV4/CTeRecepcaoEventoV4.asmx",

            # MDF-e
            "https://mdfe.svrs.rs.gov.br/ws/MDFeRecepcao/MDFeRecepcao.asmx",
            "https://mdfe.svrs.rs.gov.br/ws/MDFeRetRecepcao/MDFeRetRecepcao.asmx",
            "https://mdfe.svrs.rs.gov.br/ws/MDFeRecepcaoEvento/MDFeRecepcaoEvento.asmx",
            "https://mdfe.svrs.rs.gov.br/ws/MDFeConsulta/MDFeConsulta.asmx",
            "https://mdfe.svrs.rs.gov.br/ws/MDFeStatusServico/MDFeStatusServico.asmx",
            "https://mdfe.svrs.rs.gov.br/ws/MDFeConsNaoEnc/MDFeConsNaoEnc.asmx",
            "https://mdfe.svrs.rs.gov.br/ws/MDFeDistribuicaoDFe/MDFeDistribuicaoDFe.asmx",
            "https://mdfe.svrs.rs.gov.br/ws/MDFeRecepcaoSinc/MDFeRecepcaoSinc.asmx",
            # "https://dfe-portal.svrs.rs.gov.br/mdfe/qrCode",

            # BP-e
            "https://bpe.svrs.rs.gov.br/ws/bpeRecepcao/bpeRecepcao.asmx",
        )

        session = Session()

        session.verify = False
        for url in WSDLS:
            if not url.startswith("http"):
                url = SERVER + url
                server = SERVER
            else:
                server = "https://" + url.split("/")[2]

            session.mount(
                server,
                Pkcs12Adapter(
                    pkcs12_filename=environ["CERT_FILE"],
                    pkcs12_password=environ["CERT_PASSWORD"],
                ),
            )

            if not url.endswith("?wsdl"):
                url += "?wsdl"
            # breakpoint()
            response = session.get(url)
            filename = (
                url.split("/")[-1]
                .replace("?wsdl", "")
                .replace(".asmx", ".wsdl")
                .lower()
            )
            if "nfe" in url.lower():
                wsdl_file = os.path.join(
                    "nfelib_client", "nfe", "wsdl", "v4_0", filename
                )
            elif "mdfe" in url.lower():  # TODO move to mdfe test suite
                wsdl_file = os.path.join(
                    "nfelib_client", "mdfe", "wsdl", "v3_0", filename
                )
            elif "cte" in url.lower():  # TODO move to mdfe test suite
                wsdl_file = os.path.join(
                    "nfelib_client", "cte", "wsdl", "v4_0", filename
                )
            elif "bpe" in url.lower():
                wsdl_file = os.path.join(
                    "nfelib_client", "bpe", "wsdl", "v1_0", filename
                )
            else:
                raise ValueError(f"cannot find document kind for URL: {url} !")

            print("writing to", wsdl_file)
            print(response.text)
            with open(wsdl_file, "w") as file:
                file.write(response.text)
