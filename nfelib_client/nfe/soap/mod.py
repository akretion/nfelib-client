"""This file was generated by xsdata, v23.6, on 2023-06-24 20:51:06

Generator: DataclassGenerator
See: https://xsdata.readthedocs.io/
"""
from dataclasses import dataclass, field
from typing import Optional
from nfelib.nfe.soap.nfeautorizacao4 import (
    NfeDadosMsg as Nfeautorizacao4NfeDadosMsg,
    NfeMonitoria,
    NfeResultMsg as Nfeautorizacao4NfeResultMsg,
)
from nfelib.nfe.soap.nfeconsulta4 import (
    NfeDadosMsg as Nfeconsulta4NfeDadosMsg,
    NfeResultMsg as Nfeconsulta4NfeResultMsg,
)
from nfelib.nfe.soap.nfedistribuicaodfe import (
    NfeDistDfeInteresse,
    NfeDistDfeInteresseResponse,
)
from nfelib.nfe.soap.nfeinutilizacao4 import (
    NfeDadosMsg as Nfeinutilizacao4NfeDadosMsg,
    NfeResultMsg as Nfeinutilizacao4NfeResultMsg,
)
from nfelib.nfe.soap.nferetautorizacao4 import (
    NfeDadosMsg as Nferetautorizacao4NfeDadosMsg,
    NfeResultMsg as Nferetautorizacao4NfeResultMsg,
)
from nfelib.nfe.soap.nfestatusservico4 import (
    NfeDadosMsg as Nfestatusservico4NfeDadosMsg,
    NfeResultMsg as Nfestatusservico4NfeResultMsg,
)
from nfelib.nfe.soap.recepcaoevento4 import (
    NfeDadosMsg as Recepcaoevento4NfeDadosMsg,
    NfeResultMsg as Recepcaoevento4NfeResultMsg,
)


@dataclass
class NfeAutorizacao4SoapNfeAutorizacaoLoteZipInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfeAutorizacao4SoapNfeAutorizacaoLoteZipInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        nfeDadosMsgZip: Optional[str] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe/wsdl/NFeAutorizacao4",
            }
        )


@dataclass
class NfeAutorizacao4SoapNfeAutorizacaoLoteZipOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfeAutorizacao4SoapNfeAutorizacaoLoteZipOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )
    header: Optional["NfeAutorizacao4SoapNfeAutorizacaoLoteZipOutput.Header"] = field(
        default=None,
        metadata={
            "name": "Header",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        nfeResultMsg: Optional[Nfeautorizacao4NfeResultMsg] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe/wsdl/NFeAutorizacao4",
                "nillable": True,
            }
        )
        fault: Optional["NfeAutorizacao4SoapNfeAutorizacaoLoteZipOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

    @dataclass
    class Header:
        nfeMonitoria: Optional[NfeMonitoria] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe/wsdl/NFeAutorizacao4",
            }
        )


@dataclass
class NfeAutorizacao4SoapNfeAutorizacaoLoteInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfeAutorizacao4SoapNfeAutorizacaoLoteInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        nfeDadosMsg: Optional[Nfeautorizacao4NfeDadosMsg] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe/wsdl/NFeAutorizacao4",
            }
        )


@dataclass
class NfeAutorizacao4SoapNfeAutorizacaoLoteOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfeAutorizacao4SoapNfeAutorizacaoLoteOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )
    header: Optional["NfeAutorizacao4SoapNfeAutorizacaoLoteOutput.Header"] = field(
        default=None,
        metadata={
            "name": "Header",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        nfeResultMsg: Optional[Nfeautorizacao4NfeResultMsg] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe/wsdl/NFeAutorizacao4",
                "nillable": True,
            }
        )
        fault: Optional["NfeAutorizacao4SoapNfeAutorizacaoLoteOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )

    @dataclass
    class Header:
        nfeMonitoria: Optional[NfeMonitoria] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe/wsdl/NFeAutorizacao4",
            }
        )


@dataclass
class NfeConsultaProtocolo4SoapNfeConsultaNfInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfeConsultaProtocolo4SoapNfeConsultaNfInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        nfeDadosMsg: Optional[Nfeconsulta4NfeDadosMsg] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe/wsdl/NFeConsultaProtocolo4",
            }
        )


@dataclass
class NfeConsultaProtocolo4SoapNfeConsultaNfOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfeConsultaProtocolo4SoapNfeConsultaNfOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        nfeResultMsg: Optional[Nfeconsulta4NfeResultMsg] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe/wsdl/NFeConsultaProtocolo4",
                "nillable": True,
            }
        )
        fault: Optional["NfeConsultaProtocolo4SoapNfeConsultaNfOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )


@dataclass
class NfeDistribuicaoDfeSoapNfeDistDfeInteresseInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfeDistribuicaoDfeSoapNfeDistDfeInteresseInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        nfeDistDFeInteresse: Optional[NfeDistDfeInteresse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe/wsdl/NFeDistribuicaoDFe",
            }
        )


@dataclass
class NfeDistribuicaoDfeSoapNfeDistDfeInteresseOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfeDistribuicaoDfeSoapNfeDistDfeInteresseOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        nfeDistDFeInteresseResponse: Optional[NfeDistDfeInteresseResponse] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe/wsdl/NFeDistribuicaoDFe",
            }
        )
        fault: Optional["NfeDistribuicaoDfeSoapNfeDistDfeInteresseOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )


@dataclass
class NfeInutilizacao4SoapNfeInutilizacaoNfInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfeInutilizacao4SoapNfeInutilizacaoNfInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        nfeDadosMsg: Optional[Nfeinutilizacao4NfeDadosMsg] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe/wsdl/NFeInutilizacao4",
            }
        )


@dataclass
class NfeInutilizacao4SoapNfeInutilizacaoNfOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfeInutilizacao4SoapNfeInutilizacaoNfOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        nfeResultMsg: Optional[Nfeinutilizacao4NfeResultMsg] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe/wsdl/NFeInutilizacao4",
                "nillable": True,
            }
        )
        fault: Optional["NfeInutilizacao4SoapNfeInutilizacaoNfOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )


@dataclass
class NfeRecepcaoEvento4SoapNfeRecepcaoEventoInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfeRecepcaoEvento4SoapNfeRecepcaoEventoInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        nfeDadosMsg: Optional[Recepcaoevento4NfeDadosMsg] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe/wsdl/NFeRecepcaoEvento4",
            }
        )


@dataclass
class NfeRecepcaoEvento4SoapNfeRecepcaoEventoOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfeRecepcaoEvento4SoapNfeRecepcaoEventoOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        nfeResultMsg: Optional[Recepcaoevento4NfeResultMsg] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe/wsdl/NFeRecepcaoEvento4",
                "nillable": True,
            }
        )
        fault: Optional["NfeRecepcaoEvento4SoapNfeRecepcaoEventoOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )


@dataclass
class NfeRetAutorizacao4SoapNfeRetAutorizacaoLoteInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfeRetAutorizacao4SoapNfeRetAutorizacaoLoteInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        nfeDadosMsg: Optional[Nferetautorizacao4NfeDadosMsg] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe/wsdl/NFeRetAutorizacao4",
            }
        )


@dataclass
class NfeRetAutorizacao4SoapNfeRetAutorizacaoLoteOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfeRetAutorizacao4SoapNfeRetAutorizacaoLoteOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        nfeResultMsg: Optional[Nferetautorizacao4NfeResultMsg] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe/wsdl/NFeRetAutorizacao4",
                "nillable": True,
            }
        )
        fault: Optional["NfeRetAutorizacao4SoapNfeRetAutorizacaoLoteOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )


@dataclass
class NfeStatusServico4SoapNfeStatusServicoNfInput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfeStatusServico4SoapNfeStatusServicoNfInput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        nfeDadosMsg: Optional[Nfestatusservico4NfeDadosMsg] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe/wsdl/NFeStatusServico4",
            }
        )


@dataclass
class NfeStatusServico4SoapNfeStatusServicoNfOutput:
    class Meta:
        name = "Envelope"
        namespace = "http://schemas.xmlsoap.org/soap/envelope/"

    body: Optional["NfeStatusServico4SoapNfeStatusServicoNfOutput.Body"] = field(
        default=None,
        metadata={
            "name": "Body",
            "type": "Element",
        }
    )

    @dataclass
    class Body:
        nfeResultMsg: Optional[Nfestatusservico4NfeResultMsg] = field(
            default=None,
            metadata={
                "type": "Element",
                "namespace": "http://www.portalfiscal.inf.br/nfe/wsdl/NFeStatusServico4",
                "nillable": True,
            }
        )
        fault: Optional["NfeStatusServico4SoapNfeStatusServicoNfOutput.Body.Fault"] = field(
            default=None,
            metadata={
                "name": "Fault",
                "type": "Element",
            }
        )

        @dataclass
        class Fault:
            faultcode: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultstring: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            faultactor: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )
            detail: Optional[str] = field(
                default=None,
                metadata={
                    "type": "Element",
                    "namespace": "",
                }
            )


class NfeAutorizacao4SoapNfeAutorizacaoLote:
    style = "document"
    location = "https://nfe-homologacao.svrs.rs.gov.br/ws/NfeAutorizacao/NFeAutorizacao4.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.portalfiscal.inf.br/nfe/wsdl/NFeAutorizacao4/nfeAutorizacaoLote"
    input = NfeAutorizacao4SoapNfeAutorizacaoLoteInput
    output = NfeAutorizacao4SoapNfeAutorizacaoLoteOutput


class NfeAutorizacao4SoapNfeAutorizacaoLoteZip:
    style = "document"
    location = "https://nfe-homologacao.svrs.rs.gov.br/ws/NfeAutorizacao/NFeAutorizacao4.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.portalfiscal.inf.br/nfe/wsdl/NFeAutorizacao4/nfeAutorizacaoLoteZip"
    input = NfeAutorizacao4SoapNfeAutorizacaoLoteZipInput
    output = NfeAutorizacao4SoapNfeAutorizacaoLoteZipOutput


class NfeConsultaProtocolo4SoapNfeConsultaNf:
    style = "document"
    location = "https://nfe-homologacao.svrs.rs.gov.br/ws/NfeConsulta/NfeConsulta4.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.portalfiscal.inf.br/nfe/wsdl/NFeConsultaProtocolo4/nfeConsultaNF"
    input = NfeConsultaProtocolo4SoapNfeConsultaNfInput
    output = NfeConsultaProtocolo4SoapNfeConsultaNfOutput


class NfeDistribuicaoDfeSoapNfeDistDfeInteresse:
    style = "document"
    location = "https://www1.nfe.fazenda.gov.br/NFeDistribuicaoDFe/NFeDistribuicaoDFe.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.portalfiscal.inf.br/nfe/wsdl/NFeDistribuicaoDFe/nfeDistDFeInteresse"
    input = NfeDistribuicaoDfeSoapNfeDistDfeInteresseInput
    output = NfeDistribuicaoDfeSoapNfeDistDfeInteresseOutput


class NfeInutilizacao4SoapNfeInutilizacaoNf:
    style = "document"
    location = "https://nfe-homologacao.svrs.rs.gov.br/ws/nfeinutilizacao/nfeinutilizacao4.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.portalfiscal.inf.br/nfe/wsdl/NFeInutilizacao4/nfeInutilizacaoNF"
    input = NfeInutilizacao4SoapNfeInutilizacaoNfInput
    output = NfeInutilizacao4SoapNfeInutilizacaoNfOutput


class NfeRecepcaoEvento4SoapNfeRecepcaoEvento:
    style = "document"
    location = "https://nfe-homologacao.svrs.rs.gov.br/ws/recepcaoevento/recepcaoevento4.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.portalfiscal.inf.br/nfe/wsdl/NFeRecepcaoEvento4/nfeRecepcaoEvento"
    input = NfeRecepcaoEvento4SoapNfeRecepcaoEventoInput
    output = NfeRecepcaoEvento4SoapNfeRecepcaoEventoOutput


class NfeRetAutorizacao4SoapNfeRetAutorizacaoLote:
    style = "document"
    location = "https://nfe-homologacao.svrs.rs.gov.br/ws/NfeRetAutorizacao/NFeRetAutorizacao4.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.portalfiscal.inf.br/nfe/wsdl/NFeRetAutorizacao4/nfeRetAutorizacaoLote"
    input = NfeRetAutorizacao4SoapNfeRetAutorizacaoLoteInput
    output = NfeRetAutorizacao4SoapNfeRetAutorizacaoLoteOutput


class NfeStatusServico4SoapNfeStatusServicoNf:
    style = "document"
    location = "https://nfe-homologacao.svrs.rs.gov.br/ws/NfeStatusServico/NfeStatusServico4.asmx"
    transport = "http://schemas.xmlsoap.org/soap/http"
    soapAction = "http://www.portalfiscal.inf.br/nfe/wsdl/NFeStatusServico4/nfeStatusServicoNF"
    input = NfeStatusServico4SoapNfeStatusServicoNfInput
    output = NfeStatusServico4SoapNfeStatusServicoNfOutput
