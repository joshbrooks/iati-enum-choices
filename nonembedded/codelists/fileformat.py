from django.db import models
from django.utils.translation import pgettext_lazy


class FileFormat(models.TextChoices):
    """
    File format of published documents.
    """

    FILEFORMAT_APPLICATION_1D_INTERLEAVED_PARITYFEC = (
        "application/1d-interleaved-parityfec",
    )
    FILEFORMAT_APPLICATION_3GPDASH_QOE_REPORT_XML = (
        "application/3gpdash-qoe-report+xml",
    )
    FILEFORMAT_APPLICATION_3GPP_IMS_XML = ("application/3gpp-ims+xml",)
    FILEFORMAT_APPLICATION_A2L = ("application/A2L",)
    FILEFORMAT_APPLICATION_ACTIVEMESSAGE = ("application/activemessage",)
    FILEFORMAT_APPLICATION_ACTIVEMESSAGE = ("application/activemessage",)
    FILEFORMAT_APPLICATION_ALTOCOSTMAP_JSON = ("application/alto-costmap+json",)
    FILEFORMAT_APPLICATION_ALTOCOSTMAPFILTER_JSON = (
        "application/alto-costmapfilter+json",
    )
    FILEFORMAT_APPLICATION_ALTO_DIRECTORY_JSON = ("application/alto-directory+json",)
    FILEFORMAT_APPLICATION_ALTO_ENDPOINTPROP_JSON = (
        "application/alto-endpointprop+json",
    )
    FILEFORMAT_APPLICATION_ALTO_ENDPOINTPROPPARAMS_JSON = (
        "application/alto-endpointpropparams+json",
    )
    FILEFORMAT_APPLICATION_ALTO_ENDPOINTCOST_JSON = (
        "application/alto-endpointcost+json",
    )
    FILEFORMAT_APPLICATION_ALTO_ENDPOINTCOSTPARAMS_JSON = (
        "application/alto-endpointcostparams+json",
    )
    FILEFORMAT_APPLICATION_ALTO_ERROR_JSON = ("application/alto-error+json",)
    FILEFORMAT_APPLICATION_ALTO_NETWORKMAPFILTER_JSON = (
        "application/alto-networkmapfilter+json",
    )
    FILEFORMAT_APPLICATION_ALTO_NETWORKMAP_JSON = ("application/alto-networkmap+json",)
    FILEFORMAT_APPLICATION_AML = ("application/AML",)
    FILEFORMAT_APPLICATION_ANDREW_INSET = ("application/andrew-inset",)
    FILEFORMAT_APPLICATION_APPLEFILE = ("application/applefile",)
    FILEFORMAT_APPLICATION_ATF = ("application/ATF",)
    FILEFORMAT_APPLICATION_ATFX = ("application/ATFX",)
    FILEFORMAT_APPLICATION_ATOM_XML = ("application/atom+xml",)
    FILEFORMAT_APPLICATION_ATOMCAT_XML = ("application/atomcat+xml",)
    FILEFORMAT_APPLICATION_ATOMDELETED_XML = ("application/atomdeleted+xml",)
    FILEFORMAT_APPLICATION_ATOMICMAIL = ("application/atomicmail",)
    FILEFORMAT_APPLICATION_ATOMSVC_XML = ("application/atomsvc+xml",)
    FILEFORMAT_APPLICATION_ATXML = ("application/ATXML",)
    FILEFORMAT_APPLICATION_AUTH_POLICY_XML = ("application/auth-policy+xml",)
    FILEFORMAT_APPLICATION_BACNET_XDD_ZIP = ("application/bacnet-xdd+zip",)
    FILEFORMAT_APPLICATION_BATCH_SMTP = ("application/batch-SMTP",)
    FILEFORMAT_APPLICATION_BEEP_XML = ("application/beep+xml",)
    FILEFORMAT_APPLICATION_CALENDAR_JSON = ("application/calendar+json",)
    FILEFORMAT_APPLICATION_CALENDAR_XML = ("application/calendar+xml",)
    FILEFORMAT_APPLICATION_CALLCOMPLETION = ("application/call-completion",)
    FILEFORMAT_APPLICATION_CALS_1840 = ("application/CALS-1840",)
    FILEFORMAT_APPLICATION_CBOR = ("application/cbor",)
    FILEFORMAT_APPLICATION_CCMP_XML = ("application/ccmp+xml",)
    FILEFORMAT_APPLICATION_CCXML_XML = ("application/ccxml+xml",)
    FILEFORMAT_APPLICATION_CDFX_XML = ("application/CDFX+XML",)
    FILEFORMAT_APPLICATION_CDMICAPABILITY = ("application/cdmi-capability",)
    FILEFORMAT_APPLICATION_CDMICONTAINER = ("application/cdmi-container",)
    FILEFORMAT_APPLICATION_CDMI_DOMAIN = ("application/cdmi-domain",)
    FILEFORMAT_APPLICATION_CDMI_OBJECT = ("application/cdmi-object",)
    FILEFORMAT_APPLICATION_CDMI_QUEUE = ("application/cdmi-queue",)
    FILEFORMAT_APPLICATION_CDNI = ("application/cdni",)
    FILEFORMAT_APPLICATION_CEA = ("application/CEA",)
    FILEFORMAT_APPLICATION_CEA_2018_XML = ("application/cea-2018+xml",)
    FILEFORMAT_APPLICATION_CELLML_XML = ("application/cellml+xml",)
    FILEFORMAT_APPLICATION_CFW = ("application/cfw",)
    FILEFORMAT_APPLICATION_CLUE_INFO_XML = ("application/clue_info+xml",)
    FILEFORMAT_APPLICATION_CMS = ("application/cms",)
    FILEFORMAT_APPLICATION_CNRP_XML = ("application/cnrp+xml",)
    FILEFORMAT_APPLICATION_COAP_GROUP_JSON = ("application/coap-group+json",)
    FILEFORMAT_APPLICATION_COAP_PAYLOAD = ("application/coap-payload",)
    FILEFORMAT_APPLICATION_COMMONGROUND = ("application/commonground",)
    FILEFORMAT_APPLICATION_CONFERENCE_INFO_XML = ("application/conference-info+xml",)
    FILEFORMAT_APPLICATION_CPL_XML = ("application/cpl+xml",)
    FILEFORMAT_APPLICATION_COSE = ("application/cose",)
    FILEFORMAT_APPLICATION_COSE_KEY = ("application/cose-key",)
    FILEFORMAT_APPLICATION_COSE_KEY_SET = ("application/cose-key-set",)
    FILEFORMAT_APPLICATION_CSRATTRS = ("application/csrattrs",)
    FILEFORMAT_APPLICATION_CSTA_XML = ("application/csta+xml",)
    FILEFORMAT_APPLICATION_CSTADATA_XML = ("application/CSTAdata+xml",)
    FILEFORMAT_APPLICATION_CSVM_JSON = ("application/csvm+json",)
    FILEFORMAT_APPLICATION_CYBERCASH = ("application/cybercash",)
    FILEFORMAT_APPLICATION_DASH_XML = ("application/dash+xml",)
    FILEFORMAT_APPLICATION_DASHDELTA = ("application/dashdelta",)
    FILEFORMAT_APPLICATION_DAVMOUNT_XML = ("application/davmount+xml",)
    FILEFORMAT_APPLICATION_DCA_RFT = ("application/dca-rft",)
    FILEFORMAT_APPLICATION_DCD = ("application/DCD",)
    FILEFORMAT_APPLICATION_DEC_DX = ("application/dec-dx",)
    FILEFORMAT_APPLICATION_DIALOG_INFO_XML = ("application/dialog-info+xml",)
    FILEFORMAT_APPLICATION_DICOM = ("application/dicom",)
    FILEFORMAT_APPLICATION_DICOM_JSON = ("application/dicom+json",)
    FILEFORMAT_APPLICATION_DICOM_XML = ("application/dicom+xml",)
    FILEFORMAT_APPLICATION_DII = ("application/DII",)
    FILEFORMAT_APPLICATION_DIT = ("application/DIT",)
    FILEFORMAT_APPLICATION_DNS = ("application/dns",)
    FILEFORMAT_APPLICATION_DSKPP_XML = ("application/dskpp+xml",)
    FILEFORMAT_APPLICATION_DSSC_DER = ("application/dssc+der",)
    FILEFORMAT_APPLICATION_DSSC_XML = ("application/dssc+xml",)
    FILEFORMAT_APPLICATION_DVCS = ("application/dvcs",)
    FILEFORMAT_APPLICATION_ECMASCRIPT = ("application/ecmascript",)
    FILEFORMAT_APPLICATION_EDICONSENT = ("application/EDI-consent",)
    FILEFORMAT_APPLICATION_EDIFACT = ("application/EDIFACT",)
    FILEFORMAT_APPLICATION_EDI_X12 = ("application/EDI-X12",)
    FILEFORMAT_APPLICATION_EFI = ("application/efi",)
    FILEFORMAT_APPLICATION_EMERGENCYCALLDATA_COMMENT_XML = (
        "application/EmergencyCallData.Comment+xml",
    )
    FILEFORMAT_APPLICATION_EMERGENCYCALLDATA_CONTROL_XML = (
        "application/EmergencyCallData.Control+xml",
    )
    FILEFORMAT_APPLICATION_EMERGENCYCALLDATA_DEVICEINFO_XML = (
        "application/EmergencyCallData.DeviceInfo+xml",
    )
    FILEFORMAT_APPLICATION_EMERGENCYCALLDATA_ECALL_MSD = (
        "application/EmergencyCallData.eCall.MSD",
    )
    FILEFORMAT_APPLICATION_EMERGENCYCALLDATA_PROVIDERINFO_XML = (
        "application/EmergencyCallData.ProviderInfo+xml",
    )
    FILEFORMAT_APPLICATION_EMERGENCYCALLDATA_SERVICEINFO_XML = (
        "application/EmergencyCallData.ServiceInfo+xml",
    )
    FILEFORMAT_APPLICATION_EMERGENCYCALLDATA_SUBSCRIBERINFO_XML = (
        "application/EmergencyCallData.SubscriberInfo+xml",
    )
    FILEFORMAT_APPLICATION_EMERGENCYCALLDATA_VEDS_XML = (
        "application/EmergencyCallData.VEDS+xml",
    )
    FILEFORMAT_APPLICATION_EMMA_XML = ("application/emma+xml",)
    FILEFORMAT_APPLICATION_EMOTIONML_XML = ("application/emotionml+xml",)
    FILEFORMAT_APPLICATION_ENCAPRTP = ("application/encaprtp",)
    FILEFORMAT_APPLICATION_EPP_XML = ("application/epp+xml",)
    FILEFORMAT_APPLICATION_EPUB_ZIP = ("application/epub+zip",)
    FILEFORMAT_APPLICATION_ESHOP = ("application/eshop",)
    FILEFORMAT_APPLICATION_EXAMPLE = ("application/example",)
    FILEFORMAT_APPLICATION_EXI = ("application/exi",)
    FILEFORMAT_APPLICATION_FASTINFOSET = ("application/fastinfoset",)
    FILEFORMAT_APPLICATION_FASTSOAP = ("application/fastsoap",)
    FILEFORMAT_APPLICATION_FDT_XML = ("application/fdt+xml",)
    FILEFORMAT_APPLICATION_FITS = ("application/fits",)
    FILEFORMAT_APPLICATION_FONT_SFNT = ("application/font-sfnt",)
    FILEFORMAT_APPLICATION_FONT_TDPFR = ("application/font-tdpfr",)
    FILEFORMAT_APPLICATION_FONT_WOFF = ("application/font-woff",)
    FILEFORMAT_APPLICATION_FRAMEWORK_ATTRIBUTES_XML = (
        "application/framework-attributes+xml",
    )
    FILEFORMAT_APPLICATION_GEO_JSON = ("application/geo+json",)
    FILEFORMAT_APPLICATION_GEO_JSON_SEQ = ("application/geo+json-seq",)
    FILEFORMAT_APPLICATION_GML_XML = ("application/gml+xml",)
    FILEFORMAT_APPLICATION_GZIP = ("application/gzip",)
    FILEFORMAT_APPLICATION_H224 = ("application/H224",)
    FILEFORMAT_APPLICATION_HELD_XML = ("application/held+xml",)
    FILEFORMAT_APPLICATION_HTTP = ("application/http",)
    FILEFORMAT_APPLICATION_HYPERSTUDIO = ("application/hyperstudio",)
    FILEFORMAT_APPLICATION_IBE_KEY_REQUEST_XML = ("application/ibe-key-request+xml",)
    FILEFORMAT_APPLICATION_IBE_PKG_REPLY_XML = ("application/ibe-pkg-reply+xml",)
    FILEFORMAT_APPLICATION_IBE_PP_DATA = ("application/ibe-pp-data",)
    FILEFORMAT_APPLICATION_IGES = ("application/iges",)
    FILEFORMAT_APPLICATION_IM_ISCOMPOSING_XML = ("application/im-iscomposing+xml",)
    FILEFORMAT_APPLICATION_INDEX = ("application/index",)
    FILEFORMAT_APPLICATION_INDEX_CMD = ("application/index.cmd",)
    FILEFORMAT_APPLICATION_INDEX_OBJ = ("application/index.obj",)
    FILEFORMAT_APPLICATION_INDEX_RESPONSE = ("application/index.response",)
    FILEFORMAT_APPLICATION_INDEX_VND = ("application/index.vnd",)
    FILEFORMAT_APPLICATION_INKML_XML = ("application/inkml+xml",)
    FILEFORMAT_APPLICATION_IOTP = ("application/iotp",)
    FILEFORMAT_APPLICATION_IPFIX = ("application/ipfix",)
    FILEFORMAT_APPLICATION_IPP = ("application/ipp",)
    FILEFORMAT_APPLICATION_ISUP = ("application/isup",)
    FILEFORMAT_APPLICATION_ITS_XML = ("application/its+xml",)
    FILEFORMAT_APPLICATION_JAVASCRIPT = ("application/javascript",)
    FILEFORMAT_APPLICATION_JOSE = ("application/jose",)
    FILEFORMAT_APPLICATION_JOSE_JSON = ("application/jose+json",)
    FILEFORMAT_APPLICATION_JRD_JSON = ("application/jrd+json",)
    FILEFORMAT_APPLICATION_JSON = ("application/json",)
    FILEFORMAT_APPLICATION_JSON_PATCH_JSON = ("application/json-patch+json",)
    FILEFORMAT_APPLICATION_JSON_SEQ = ("application/json-seq",)
    FILEFORMAT_APPLICATION_JWK_JSON = ("application/jwk+json",)
    FILEFORMAT_APPLICATION_JWK_SET_JSON = ("application/jwk-set+json",)
    FILEFORMAT_APPLICATION_JWT = ("application/jwt",)
    FILEFORMAT_APPLICATION_KPML_REQUEST_XML = ("application/kpml-request+xml",)
    FILEFORMAT_APPLICATION_KPML_RESPONSE_XML = ("application/kpml-response+xml",)
    FILEFORMAT_APPLICATION_LD_JSON = ("application/ld+json",)
    FILEFORMAT_APPLICATION_LGR_XML = ("application/lgr+xml",)
    FILEFORMAT_APPLICATION_LINK_FORMAT = ("application/link-format",)
    FILEFORMAT_APPLICATION_LOADCONTROL_XML = ("application/load-control+xml",)
    FILEFORMAT_APPLICATION_LOST_XML = ("application/lost+xml",)
    FILEFORMAT_APPLICATION_LOSTSYNC_XML = ("application/lostsync+xml",)
    FILEFORMAT_APPLICATION_LXF = ("application/LXF",)
    FILEFORMAT_APPLICATION_MAC_BINHEX40 = ("application/mac-binhex40",)
    FILEFORMAT_APPLICATION_MACWRITEII = ("application/macwriteii",)
    FILEFORMAT_APPLICATION_MADS_XML = ("application/mads+xml",)
    FILEFORMAT_APPLICATION_MARC = ("application/marc",)
    FILEFORMAT_APPLICATION_MARCXML_XML = ("application/marcxml+xml",)
    FILEFORMAT_APPLICATION_MATHEMATICA = ("application/mathematica",)
    FILEFORMAT_APPLICATION_MATHMLCONTENT_XML = ("application/mathml-content+xml",)
    FILEFORMAT_APPLICATION_MATHML_PRESENTATION_XML = (
        "application/mathml-presentation+xml",
    )
    FILEFORMAT_APPLICATION_MATHML_XML = ("application/mathml+xml",)
    FILEFORMAT_APPLICATION_MBMS_ASSOCIATED_PROCEDURE_DESCRIPTION_XML = (
        "application/mbms-associated-procedure-description+xml",
    )
    FILEFORMAT_APPLICATION_MBMS_DEREGISTER_XML = ("application/mbms-deregister+xml",)
    FILEFORMAT_APPLICATION_MBMS_ENVELOPE_XML = ("application/mbms-envelope+xml",)
    FILEFORMAT_APPLICATION_MBMS_MSK_RESPONSE_XML = (
        "application/mbms-msk-response+xml",
    )
    FILEFORMAT_APPLICATION_MBMS_MSK_XML = ("application/mbms-msk+xml",)
    FILEFORMAT_APPLICATION_MBMS_PROTECTION_DESCRIPTION_XML = (
        "application/mbms-protection-description+xml",
    )
    FILEFORMAT_APPLICATION_MBMS_RECEPTION_REPORT_XML = (
        "application/mbms-reception-report+xml",
    )
    FILEFORMAT_APPLICATION_MBMS_REGISTER_RESPONSE_XML = (
        "application/mbms-register-response+xml",
    )
    FILEFORMAT_APPLICATION_MBMS_REGISTER_XML = ("application/mbms-register+xml",)
    FILEFORMAT_APPLICATION_MBMS_SCHEDULE_XML = ("application/mbms-schedule+xml",)
    FILEFORMAT_APPLICATION_MBMS_USER_SERVICE_DESCRIPTION_XML = (
        "application/mbms-user-service-description+xml",
    )
    FILEFORMAT_APPLICATION_MBOX = ("application/mbox",)
    FILEFORMAT_APPLICATION_MEDIA_CONTROL_XML = ("application/media_control+xml",)
    FILEFORMAT_APPLICATION_MEDIA_POLICY_DATASET_XML = (
        "application/media-policy-dataset+xml",
    )
    FILEFORMAT_APPLICATION_MEDIASERVERCONTROL_XML = (
        "application/mediaservercontrol+xml",
    )
    FILEFORMAT_APPLICATION_MERGE_PATCH_JSON = ("application/merge-patch+json",)
    FILEFORMAT_APPLICATION_METALINK4_XML = ("application/metalink4+xml",)
    FILEFORMAT_APPLICATION_METS_XML = ("application/mets+xml",)
    FILEFORMAT_APPLICATION_MF4 = ("application/MF4",)
    FILEFORMAT_APPLICATION_MIKEY = ("application/mikey",)
    FILEFORMAT_APPLICATION_MODS_XML = ("application/mods+xml",)
    FILEFORMAT_APPLICATION_MOSS_KEYS = ("application/moss-keys",)
    FILEFORMAT_APPLICATION_MOSS_SIGNATURE = ("application/moss-signature",)
    FILEFORMAT_APPLICATION_MOSSKEY_DATA = ("application/mosskey-data",)
    FILEFORMAT_APPLICATION_MOSSKEY_REQUEST = ("application/mosskey-request",)
    FILEFORMAT_APPLICATION_MP21 = ("application/mp21",)
    FILEFORMAT_APPLICATION_MP4 = ("application/mp4",)
    FILEFORMAT_APPLICATION_MPEG4_GENERIC = ("application/mpeg4-generic",)
    FILEFORMAT_APPLICATION_MPEG4_IOD = ("application/mpeg4-iod",)
    FILEFORMAT_APPLICATION_MPEG4_IOD_XMT = ("application/mpeg4-iod-xmt",)
    FILEFORMAT_APPLICATION_MRBCONSUMER_XML = ("application/mrb-consumer+xml",)
    FILEFORMAT_APPLICATION_MRB_PUBLISH_XML = ("application/mrb-publish+xml",)
    FILEFORMAT_APPLICATION_MSC_IVR_XML = ("application/msc-ivr+xml",)
    FILEFORMAT_APPLICATION_MSC_MIXER_XML = ("application/msc-mixer+xml",)
    FILEFORMAT_APPLICATION_MSWORD = ("application/msword",)
    FILEFORMAT_APPLICATION_MUD_JSON = ("application/mud+json",)
    FILEFORMAT_APPLICATION_MXF = ("application/mxf",)
    FILEFORMAT_APPLICATION_N_QUADS = ("application/n-quads",)
    FILEFORMAT_APPLICATION_N_TRIPLES = ("application/n-triples",)
    FILEFORMAT_APPLICATION_NASDATA = ("application/nasdata",)
    FILEFORMAT_APPLICATION_NEWSCHECKGROUPS = ("application/news-checkgroups",)
    FILEFORMAT_APPLICATION_NEWS_GROUPINFO = ("application/news-groupinfo",)
    FILEFORMAT_APPLICATION_NEWS_TRANSMISSION = ("application/news-transmission",)
    FILEFORMAT_APPLICATION_NLSML_XML = ("application/nlsml+xml",)
    FILEFORMAT_APPLICATION_NSS = ("application/nss",)
    FILEFORMAT_APPLICATION_OCSP_REQUEST = ("application/ocsp-request",)
    FILEFORMAT_APPLICATION_OCSP_RESPONSE = ("application/ocsp-response",)
    FILEFORMAT_APPLICATION_OCTET_STREAM = ("application/octet-stream",)
    FILEFORMAT_APPLICATION_ODA = ("application/oda",)
    FILEFORMAT_APPLICATION_ODX = ("application/ODX",)
    FILEFORMAT_APPLICATION_OEBPS_PACKAGE_XML = ("application/oebps-package+xml",)
    FILEFORMAT_APPLICATION_OGG = ("application/ogg",)
    FILEFORMAT_APPLICATION_OXPS = ("application/oxps",)
    FILEFORMAT_APPLICATION_P2P_OVERLAY_XML = ("application/p2p-overlay+xml",)
    FILEFORMAT_APPLICATION_PARITYFEC = ("application/parityfec",)
    FILEFORMAT_APPLICATION_PATCH_OPS_ERROR_XML = ("application/patch-ops-error+xml",)
    FILEFORMAT_APPLICATION_PDF = ("application/pdf",)
    FILEFORMAT_APPLICATION_PDX = ("application/PDX",)
    FILEFORMAT_APPLICATION_PGP_ENCRYPTED = ("application/pgp-encrypted",)
    FILEFORMAT_APPLICATION_PGP_KEYS = ("application/pgp-keys",)
    FILEFORMAT_APPLICATION_PGP_SIGNATURE = ("application/pgp-signature",)
    FILEFORMAT_APPLICATION_PIDF_DIFF_XML = ("application/pidf-diff+xml",)
    FILEFORMAT_APPLICATION_PIDF_XML = ("application/pidf+xml",)
    FILEFORMAT_APPLICATION_PKCS10 = ("application/pkcs10",)
    FILEFORMAT_APPLICATION_PKCS7_MIME = ("application/pkcs7-mime",)
    FILEFORMAT_APPLICATION_PKCS7_SIGNATURE = ("application/pkcs7-signature",)
    FILEFORMAT_APPLICATION_PKCS8 = ("application/pkcs8",)
    FILEFORMAT_APPLICATION_PKCS12 = ("application/pkcs12",)
    FILEFORMAT_APPLICATION_PKIX_ATTRCERT = ("application/pkix-attr-cert",)
    FILEFORMAT_APPLICATION_PKIXCERT = ("application/pkix-cert",)
    FILEFORMAT_APPLICATION_PKIXCRL = ("application/pkix-crl",)
    FILEFORMAT_APPLICATION_PKIX_PKIPATH = ("application/pkix-pkipath",)
    FILEFORMAT_APPLICATION_PKIXCMP = ("application/pkixcmp",)
    FILEFORMAT_APPLICATION_PLS_XML = ("application/pls+xml",)
    FILEFORMAT_APPLICATION_POC_SETTINGS_XML = ("application/poc-settings+xml",)
    FILEFORMAT_APPLICATION_POSTSCRIPT = ("application/postscript",)
    FILEFORMAT_APPLICATION_PPSP_TRACKER_JSON = ("application/ppsp-tracker+json",)
    FILEFORMAT_APPLICATION_PROBLEM_JSON = ("application/problem+json",)
    FILEFORMAT_APPLICATION_PROBLEM_XML = ("application/problem+xml",)
    FILEFORMAT_APPLICATION_PROVENANCE_XML = ("application/provenance+xml",)
    FILEFORMAT_APPLICATION_PRS_ALVESTRAND_TITRAX_SHEET = (
        "application/prs.alvestrand.titrax-sheet",
    )
    FILEFORMAT_APPLICATION_PRS_CWW = ("application/prs.cww",)
    FILEFORMAT_APPLICATION_PRS_HPUB_ZIP = ("application/prs.hpub+zip",)
    FILEFORMAT_APPLICATION_PRS_NPREND = ("application/prs.nprend",)
    FILEFORMAT_APPLICATION_PRS_PLUCKER = ("application/prs.plucker",)
    FILEFORMAT_APPLICATION_PRS_RDF_XMLCRYPT = ("application/prs.rdf-xml-crypt",)
    FILEFORMAT_APPLICATION_PRS_XSF_XML = ("application/prs.xsf+xml",)
    FILEFORMAT_APPLICATION_PSKC_XML = ("application/pskc+xml",)
    FILEFORMAT_APPLICATION_RDF_XML = ("application/rdf+xml",)
    FILEFORMAT_APPLICATION_QSIG = ("application/qsig",)
    FILEFORMAT_APPLICATION_RAPTORFEC = ("application/raptorfec",)
    FILEFORMAT_APPLICATION_RDAP_JSON = ("application/rdap+json",)
    FILEFORMAT_APPLICATION_REGINFO_XML = ("application/reginfo+xml",)
    FILEFORMAT_APPLICATION_RELAX_NGCOMPACT_SYNTAX = (
        "application/relax-ng-compact-syntax",
    )
    FILEFORMAT_APPLICATION_REMOTE_PRINTING = ("application/remote-printing",)
    FILEFORMAT_APPLICATION_REPUTON_JSON = ("application/reputon+json",)
    FILEFORMAT_APPLICATION_RESOURCE_LISTS_DIFF_XML = (
        "application/resource-lists-diff+xml",
    )
    FILEFORMAT_APPLICATION_RESOURCE_LISTS_XML = ("application/resource-lists+xml",)
    FILEFORMAT_APPLICATION_RFC_XML = ("application/rfc+xml",)
    FILEFORMAT_APPLICATION_RISCOS = ("application/riscos",)
    FILEFORMAT_APPLICATION_RLMI_XML = ("application/rlmi+xml",)
    FILEFORMAT_APPLICATION_RLS_SERVICES_XML = ("application/rls-services+xml",)
    FILEFORMAT_APPLICATION_RPKI_GHOSTBUSTERS = ("application/rpki-ghostbusters",)
    FILEFORMAT_APPLICATION_RPKI_MANIFEST = ("application/rpki-manifest",)
    FILEFORMAT_APPLICATION_RPKI_PUBLICATION = ("application/rpki-publication",)
    FILEFORMAT_APPLICATION_RPKI_ROA = ("application/rpki-roa",)
    FILEFORMAT_APPLICATION_RPKI_UPDOWN = ("application/rpki-updown",)
    FILEFORMAT_APPLICATION_RTF = ("application/rtf",)
    FILEFORMAT_APPLICATION_RTPLOOPBACK = ("application/rtploopback",)
    FILEFORMAT_APPLICATION_RTX = ("application/rtx",)
    FILEFORMAT_APPLICATION_SAMLASSERTION_XML = ("application/samlassertion+xml",)
    FILEFORMAT_APPLICATION_SAMLMETADATA_XML = ("application/samlmetadata+xml",)
    FILEFORMAT_APPLICATION_SBML_XML = ("application/sbml+xml",)
    FILEFORMAT_APPLICATION_SCAIP_XML = ("application/scaip+xml",)
    FILEFORMAT_APPLICATION_SCIM_JSON = ("application/scim+json",)
    FILEFORMAT_APPLICATION_SCVPCV_REQUEST = ("application/scvp-cv-request",)
    FILEFORMAT_APPLICATION_SCVPCV_RESPONSE = ("application/scvp-cv-response",)
    FILEFORMAT_APPLICATION_SCVP_VP_REQUEST = ("application/scvp-vp-request",)
    FILEFORMAT_APPLICATION_SCVP_VP_RESPONSE = ("application/scvp-vp-response",)
    FILEFORMAT_APPLICATION_SDP = ("application/sdp",)
    FILEFORMAT_APPLICATION_SEP_EXI = ("application/sep-exi",)
    FILEFORMAT_APPLICATION_SEP_XML = ("application/sep+xml",)
    FILEFORMAT_APPLICATION_SESSION_INFO = ("application/session-info",)
    FILEFORMAT_APPLICATION_SET_PAYMENT = ("application/set-payment",)
    FILEFORMAT_APPLICATION_SET_PAYMENT_INITIATION = (
        "application/set-payment-initiation",
    )
    FILEFORMAT_APPLICATION_SET_REGISTRATION = ("application/set-registration",)
    FILEFORMAT_APPLICATION_SET_REGISTRATION_INITIATION = (
        "application/set-registration-initiation",
    )
    FILEFORMAT_APPLICATION_SGML = ("application/sgml",)
    FILEFORMAT_APPLICATION_SGML_OPENCATALOG = ("application/sgml-open-catalog",)
    FILEFORMAT_APPLICATION_SHF_XML = ("application/shf+xml",)
    FILEFORMAT_APPLICATION_SIEVE = ("application/sieve",)
    FILEFORMAT_APPLICATION_SIMPLE_FILTER_XML = ("application/simple-filter+xml",)
    FILEFORMAT_APPLICATION_SIMPLE_MESSAGE_SUMMARY = (
        "application/simple-message-summary",
    )
    FILEFORMAT_APPLICATION_SIMPLESYMBOLCONTAINER = (
        "application/simpleSymbolContainer",
    )
    FILEFORMAT_APPLICATION_SLATE = ("application/slate",)
    FILEFORMAT_APPLICATION_SMIL = ("application/smil",)
    FILEFORMAT_APPLICATION_SMIL_XML = ("application/smil+xml",)
    FILEFORMAT_APPLICATION_SMPTE336M = ("application/smpte336m",)
    FILEFORMAT_APPLICATION_SOAP_FASTINFOSET = ("application/soap+fastinfoset",)
    FILEFORMAT_APPLICATION_SOAP_XML = ("application/soap+xml",)
    FILEFORMAT_APPLICATION_SPARQL_QUERY = ("application/sparql-query",)
    FILEFORMAT_APPLICATION_SPARQL_RESULTS_XML = ("application/sparql-results+xml",)
    FILEFORMAT_APPLICATION_SPIRITS_EVENT_XML = ("application/spirits-event+xml",)
    FILEFORMAT_APPLICATION_SQL = ("application/sql",)
    FILEFORMAT_APPLICATION_SRGS = ("application/srgs",)
    FILEFORMAT_APPLICATION_SRGS_XML = ("application/srgs+xml",)
    FILEFORMAT_APPLICATION_SRU_XML = ("application/sru+xml",)
    FILEFORMAT_APPLICATION_SSML_XML = ("application/ssml+xml",)
    FILEFORMAT_APPLICATION_TAMP_APEX_UPDATE = ("application/tamp-apex-update",)
    FILEFORMAT_APPLICATION_TAMP_APEX_UPDATECONFIRM = (
        "application/tamp-apex-update-confirm",
    )
    FILEFORMAT_APPLICATION_TAMPCOMMUNITY_UPDATE = ("application/tamp-community-update",)
    FILEFORMAT_APPLICATION_TAMPCOMMUNITY_UPDATECONFIRM = (
        "application/tamp-community-update-confirm",
    )
    FILEFORMAT_APPLICATION_TAMP_ERROR = ("application/tamp-error",)
    FILEFORMAT_APPLICATION_TAMP_SEQUENCE_ADJUST = ("application/tamp-sequence-adjust",)
    FILEFORMAT_APPLICATION_TAMP_SEQUENCE_ADJUSTCONFIRM = (
        "application/tamp-sequence-adjust-confirm",
    )
    FILEFORMAT_APPLICATION_TAMP_STATUS_QUERY = ("application/tamp-status-query",)
    FILEFORMAT_APPLICATION_TAMP_STATUS_RESPONSE = ("application/tamp-status-response",)
    FILEFORMAT_APPLICATION_TAMP_UPDATE = ("application/tamp-update",)
    FILEFORMAT_APPLICATION_TAMP_UPDATECONFIRM = ("application/tamp-update-confirm",)
    FILEFORMAT_APPLICATION_TEI_XML = ("application/tei+xml",)
    FILEFORMAT_APPLICATION_THRAUD_XML = ("application/thraud+xml",)
    FILEFORMAT_APPLICATION_TIMESTAMP_QUERY = ("application/timestamp-query",)
    FILEFORMAT_APPLICATION_TIMESTAMP_REPLY = ("application/timestamp-reply",)
    FILEFORMAT_APPLICATION_TIMESTAMPED_DATA = ("application/timestamped-data",)
    FILEFORMAT_APPLICATION_TRIG = ("application/trig",)
    FILEFORMAT_APPLICATION_TTML_XML = ("application/ttml+xml",)
    FILEFORMAT_APPLICATION_TVE_TRIGGER = ("application/tve-trigger",)
    FILEFORMAT_APPLICATION_ULPFEC = ("application/ulpfec",)
    FILEFORMAT_APPLICATION_URC_GRPSHEET_XML = ("application/urc-grpsheet+xml",)
    FILEFORMAT_APPLICATION_URC_RESSHEET_XML = ("application/urc-ressheet+xml",)
    FILEFORMAT_APPLICATION_URC_TARGETDESC_XML = ("application/urc-targetdesc+xml",)
    FILEFORMAT_APPLICATION_URC_UISOCKETDESC_XML = ("application/urc-uisocketdesc+xml",)
    FILEFORMAT_APPLICATION_VCARD_JSON = ("application/vcard+json",)
    FILEFORMAT_APPLICATION_VCARD_XML = ("application/vcard+xml",)
    FILEFORMAT_APPLICATION_VEMMI = ("application/vemmi",)
    FILEFORMAT_APPLICATION_VND_1000MINDS_DECISION_MODEL_XML = (
        "application/vnd.1000minds.decision-model+xml",
    )
    FILEFORMAT_APPLICATION_VND_3GPP_ACCESS_TRANSFER_EVENTS_XML = (
        "application/vnd.3gpp.access-transfer-events+xml",
    )
    FILEFORMAT_APPLICATION_VND_3GPP_BSF_XML = ("application/vnd.3gpp.bsf+xml",)
    FILEFORMAT_APPLICATION_VND_3GPP_MIDCALL_XML = ("application/vnd.3gpp.mid-call+xml",)
    FILEFORMAT_APPLICATION_VND_3GPP_PIC_BW_LARGE = (
        "application/vnd.3gpp.pic-bw-large",
    )
    FILEFORMAT_APPLICATION_VND_3GPP_PIC_BW_SMALL = (
        "application/vnd.3gpp.pic-bw-small",
    )
    FILEFORMAT_APPLICATION_VND_3GPP_PIC_BW_VAR = ("application/vnd.3gpp.pic-bw-var",)
    FILEFORMAT_APPLICATION_VND_3GPP_PROSE_PC3CH_XML = (
        "application/vnd.3gpp-prose-pc3ch+xml",
    )
    FILEFORMAT_APPLICATION_VND_3GPP_PROSE_XML = ("application/vnd.3gpp-prose+xml",)
    FILEFORMAT_APPLICATION_VND_3GPP_SMS = ("application/vnd.3gpp.sms",)
    FILEFORMAT_APPLICATION_VND_3GPP_SMS_XML = ("application/vnd.3gpp.sms+xml",)
    FILEFORMAT_APPLICATION_VND_3GPP_SRVCC_EXT_XML = (
        "application/vnd.3gpp.srvcc-ext+xml",
    )
    FILEFORMAT_APPLICATION_VND_3GPP_SRVCC_INFO_XML = (
        "application/vnd.3gpp.SRVCC-info+xml",
    )
    FILEFORMAT_APPLICATION_VND_3GPP_STATE_AND_EVENT_INFO_XML = (
        "application/vnd.3gpp.state-and-event-info+xml",
    )
    FILEFORMAT_APPLICATION_VND_3GPP_USSD_XML = ("application/vnd.3gpp.ussd+xml",)
    FILEFORMAT_APPLICATION_VND_3GPP2_BCMCSINFO_XML = (
        "application/vnd.3gpp2.bcmcsinfo+xml",
    )
    FILEFORMAT_APPLICATION_VND_3GPP2_SMS = ("application/vnd.3gpp2.sms",)
    FILEFORMAT_APPLICATION_VND_3GPP2_TCAP = ("application/vnd.3gpp2.tcap",)
    FILEFORMAT_APPLICATION_VND_3LIGHTSSOFTWARE_IMAGESCAL = (
        "application/vnd.3lightssoftware.imagescal",
    )
    FILEFORMAT_APPLICATION_VND_3M_POST_IT_NOTES = ("application/vnd.3M.Post-it-Notes",)
    FILEFORMAT_APPLICATION_VND_ACCPAC_SIMPLY_ASO = (
        "application/vnd.accpac.simply.aso",
    )
    FILEFORMAT_APPLICATION_VND_ACCPAC_SIMPLY_IMP = (
        "application/vnd.accpac.simply.imp",
    )
    FILEFORMAT_APPLICATION_VND_ACUCOBOL = ("application/vnd.acucobol",)
    FILEFORMAT_APPLICATION_VND_ACUCORP = ("application/vnd.acucorp",)
    FILEFORMAT_APPLICATION_VND_ADOBE_FLASH_MOVIE = (
        "application/vnd.adobe.flash.movie",
    )
    FILEFORMAT_APPLICATION_VND_ADOBE_FORMSCENTRAL_FCDT = (
        "application/vnd.adobe.formscentral.fcdt",
    )
    FILEFORMAT_APPLICATION_VND_ADOBE_FXP = ("application/vnd.adobe.fxp",)
    FILEFORMAT_APPLICATION_VND_ADOBE_PARTIAL_UPLOAD = (
        "application/vnd.adobe.partial-upload",
    )
    FILEFORMAT_APPLICATION_VND_ADOBE_XDP_XML = ("application/vnd.adobe.xdp+xml",)
    FILEFORMAT_APPLICATION_VND_ADOBE_XFDF = ("application/vnd.adobe.xfdf",)
    FILEFORMAT_APPLICATION_VND_AETHER_IMP = ("application/vnd.aether.imp",)
    FILEFORMAT_APPLICATION_VND_AH_BARCODE = ("application/vnd.ah-barcode",)
    FILEFORMAT_APPLICATION_VND_AHEAD_SPACE = ("application/vnd.ahead.space",)
    FILEFORMAT_APPLICATION_VND_AIRZIP_FILESECURE_AZF = (
        "application/vnd.airzip.filesecure.azf",
    )
    FILEFORMAT_APPLICATION_VND_AIRZIP_FILESECURE_AZS = (
        "application/vnd.airzip.filesecure.azs",
    )
    FILEFORMAT_APPLICATION_VND_AMAZON_MOBI8_EBOOK = (
        "application/vnd.amazon.mobi8-ebook",
    )
    FILEFORMAT_APPLICATION_VND_AMERICANDYNAMICS_ACC = (
        "application/vnd.americandynamics.acc",
    )
    FILEFORMAT_APPLICATION_VND_AMIGA_AMI = ("application/vnd.amiga.ami",)
    FILEFORMAT_APPLICATION_VND_AMUNDSEN_MAZE_XML = (
        "application/vnd.amundsen.maze+xml",
    )
    FILEFORMAT_APPLICATION_VND_ANKI = ("application/vnd.anki",)
    FILEFORMAT_APPLICATION_VND_ANSER_WEBCERTIFICATE_ISSUE_INITIATION = (
        "application/vnd.anser-web-certificate-issue-initiation",
    )
    FILEFORMAT_APPLICATION_VND_ANTIX_GAMECOMPONENT = (
        "application/vnd.antix.game-component",
    )
    FILEFORMAT_APPLICATION_VND_APACHE_THRIFT_BINARY = (
        "application/vnd.apache.thrift.binary",
    )
    FILEFORMAT_APPLICATION_VND_APACHE_THRIFT_COMPACT = (
        "application/vnd.apache.thrift.compact",
    )
    FILEFORMAT_APPLICATION_VND_APACHE_THRIFT_JSON = (
        "application/vnd.apache.thrift.json",
    )
    FILEFORMAT_APPLICATION_VND_API_JSON = ("application/vnd.api+json",)
    FILEFORMAT_APPLICATION_VND_APOTHEKENDE_RESERVATION_JSON = (
        "application/vnd.apothekende.reservation+json",
    )
    FILEFORMAT_APPLICATION_VND_APPLE_MPEGURL = ("application/vnd.apple.mpegurl",)
    FILEFORMAT_APPLICATION_VND_APPLE_INSTALLER_XML = (
        "application/vnd.apple.installer+xml",
    )
    FILEFORMAT_APPLICATION_VND_ARASTRA_SWI = ("application/vnd.arastra.swi",)
    FILEFORMAT_APPLICATION_VND_ARISTANETWORKS_SWI = (
        "application/vnd.aristanetworks.swi",
    )
    FILEFORMAT_APPLICATION_VND_ARTSQUARE = ("application/vnd.artsquare",)
    FILEFORMAT_APPLICATION_VND_ASTRAEA_SOFTWARE_IOTA = (
        "application/vnd.astraea-software.iota",
    )
    FILEFORMAT_APPLICATION_VND_AUDIOGRAPH = ("application/vnd.audiograph",)
    FILEFORMAT_APPLICATION_VND_AUTOPACKAGE = ("application/vnd.autopackage",)
    FILEFORMAT_APPLICATION_VND_AVISTAR_XML = ("application/vnd.avistar+xml",)
    FILEFORMAT_APPLICATION_VND_BALSAMIQ_BMML_XML = (
        "application/vnd.balsamiq.bmml+xml",
    )
    FILEFORMAT_APPLICATION_VND_BALSAMIQ_BMPR = ("application/vnd.balsamiq.bmpr",)
    FILEFORMAT_APPLICATION_VND_BEKITZUR_STECH_JSON = (
        "application/vnd.bekitzur-stech+json",
    )
    FILEFORMAT_APPLICATION_VND_BINT_MEDCONTENT = ("application/vnd.bint.med-content",)
    FILEFORMAT_APPLICATION_VND_BIOPAX_RDF_XML = ("application/vnd.biopax.rdf+xml",)
    FILEFORMAT_APPLICATION_VND_BLUEICE_MULTIPASS = (
        "application/vnd.blueice.multipass",
    )
    FILEFORMAT_APPLICATION_VND_BLUETOOTH_EP_OOB = ("application/vnd.bluetooth.ep.oob",)
    FILEFORMAT_APPLICATION_VND_BLUETOOTH_LE_OOB = ("application/vnd.bluetooth.le.oob",)
    FILEFORMAT_APPLICATION_VND_BMI = ("application/vnd.bmi",)
    FILEFORMAT_APPLICATION_VND_BUSINESSOBJECTS = ("application/vnd.businessobjects",)
    FILEFORMAT_APPLICATION_VND_CAB_JSCRIPT = ("application/vnd.cab-jscript",)
    FILEFORMAT_APPLICATION_VND_CANONCPDL = ("application/vnd.canon-cpdl",)
    FILEFORMAT_APPLICATION_VND_CANON_LIPS = ("application/vnd.canon-lips",)
    FILEFORMAT_APPLICATION_VND_CAPASYSTEMS_PG_JSON = (
        "application/vnd.capasystems-pg+json",
    )
    FILEFORMAT_APPLICATION_VND_CENDIO_THINLINC_CLIENTCONF = (
        "application/vnd.cendio.thinlinc.clientconf",
    )
    FILEFORMAT_APPLICATION_VND_CENTURY_SYSTEMS_TCP_STREAM = (
        "application/vnd.century-systems.tcp_stream",
    )
    FILEFORMAT_APPLICATION_VND_CHEMDRAW_XML = ("application/vnd.chemdraw+xml",)
    FILEFORMAT_APPLICATION_VND_CHESS_PGN = ("application/vnd.chess-pgn",)
    FILEFORMAT_APPLICATION_VND_CHIPNUTS_KARAOKE_MMD = (
        "application/vnd.chipnuts.karaoke-mmd",
    )
    FILEFORMAT_APPLICATION_VND_CINDERELLA = ("application/vnd.cinderella",)
    FILEFORMAT_APPLICATION_VND_CIRPACK_ISDN_EXT = ("application/vnd.cirpack.isdn-ext",)
    FILEFORMAT_APPLICATION_VND_CITATIONSTYLES_STYLE_XML = (
        "application/vnd.citationstyles.style+xml",
    )
    FILEFORMAT_APPLICATION_VND_CLAYMORE = ("application/vnd.claymore",)
    FILEFORMAT_APPLICATION_VND_CLOANTO_RP9 = ("application/vnd.cloanto.rp9",)
    FILEFORMAT_APPLICATION_VND_CLONK_C4GROUP = ("application/vnd.clonk.c4group",)
    FILEFORMAT_APPLICATION_VND_CLUETRUST_CARTOMOBILECONFIG = (
        "application/vnd.cluetrust.cartomobile-config",
    )
    FILEFORMAT_APPLICATION_VND_CLUETRUST_CARTOMOBILECONFIG_PKG = (
        "application/vnd.cluetrust.cartomobile-config-pkg",
    )
    FILEFORMAT_APPLICATION_VND_COFFEESCRIPT = ("application/vnd.coffeescript",)
    FILEFORMAT_APPLICATION_VND_COLLECTION_DOC_JSON = (
        "application/vnd.collection.doc+json",
    )
    FILEFORMAT_APPLICATION_VND_COLLECTION_JSON = ("application/vnd.collection+json",)
    FILEFORMAT_APPLICATION_VND_COLLECTION_NEXT_JSON = (
        "application/vnd.collection.next+json",
    )
    FILEFORMAT_APPLICATION_VND_COMICBOOK_ZIP = ("application/vnd.comicbook+zip",)
    FILEFORMAT_APPLICATION_VND_COMMERCE_BATTELLE = (
        "application/vnd.commerce-battelle",
    )
    FILEFORMAT_APPLICATION_VND_COMMONSPACE = ("application/vnd.commonspace",)
    FILEFORMAT_APPLICATION_VND_COREOS_IGNITION_JSON = (
        "application/vnd.coreos.ignition+json",
    )
    FILEFORMAT_APPLICATION_VND_COSMOCALLER = ("application/vnd.cosmocaller",)
    FILEFORMAT_APPLICATION_VND_CONTACT_CMSG = ("application/vnd.contact.cmsg",)
    FILEFORMAT_APPLICATION_VND_CRICK_CLICKER = ("application/vnd.crick.clicker",)
    FILEFORMAT_APPLICATION_VND_CRICK_CLICKER_KEYBOARD = (
        "application/vnd.crick.clicker.keyboard",
    )
    FILEFORMAT_APPLICATION_VND_CRICK_CLICKER_PALETTE = (
        "application/vnd.crick.clicker.palette",
    )
    FILEFORMAT_APPLICATION_VND_CRICK_CLICKER_TEMPLATE = (
        "application/vnd.crick.clicker.template",
    )
    FILEFORMAT_APPLICATION_VND_CRICK_CLICKER_WORDBANK = (
        "application/vnd.crick.clicker.wordbank",
    )
    FILEFORMAT_APPLICATION_VND_CRITICALTOOLS_WBS_XML = (
        "application/vnd.criticaltools.wbs+xml",
    )
    FILEFORMAT_APPLICATION_VND_CTC_POSML = ("application/vnd.ctc-posml",)
    FILEFORMAT_APPLICATION_VND_CTCT_WS_XML = ("application/vnd.ctct.ws+xml",)
    FILEFORMAT_APPLICATION_VND_CUPS_PDF = ("application/vnd.cups-pdf",)
    FILEFORMAT_APPLICATION_VND_CUPS_POSTSCRIPT = ("application/vnd.cups-postscript",)
    FILEFORMAT_APPLICATION_VND_CUPS_PPD = ("application/vnd.cups-ppd",)
    FILEFORMAT_APPLICATION_VND_CUPS_RASTER = ("application/vnd.cups-raster",)
    FILEFORMAT_APPLICATION_VND_CUPS_RAW = ("application/vnd.cups-raw",)
    FILEFORMAT_APPLICATION_VND_CURL = ("application/vnd.curl",)
    FILEFORMAT_APPLICATION_VND_CYAN_DEAN_ROOT_XML = (
        "application/vnd.cyan.dean.root+xml",
    )
    FILEFORMAT_APPLICATION_VND_CYBANK = ("application/vnd.cybank",)
    FILEFORMAT_APPLICATION_VND_D2L_COURSEPACKAGE1P0_ZIP = (
        "application/vnd.d2l.coursepackage1p0+zip",
    )
    FILEFORMAT_APPLICATION_VND_DART = ("application/vnd.dart",)
    FILEFORMAT_APPLICATION_VND_DATA_VISION_RDZ = ("application/vnd.data-vision.rdz",)
    FILEFORMAT_APPLICATION_VND_DATAPACKAGE_JSON = ("application/vnd.datapackage+json",)
    FILEFORMAT_APPLICATION_VND_DATARESOURCE_JSON = (
        "application/vnd.dataresource+json",
    )
    FILEFORMAT_APPLICATION_VND_DEBIAN_BINARY_PACKAGE = (
        "application/vnd.debian.binary-package",
    )
    FILEFORMAT_APPLICATION_VND_DECE_DATA = ("application/vnd.dece.data",)
    FILEFORMAT_APPLICATION_VND_DECE_TTML_XML = ("application/vnd.dece.ttml+xml",)
    FILEFORMAT_APPLICATION_VND_DECE_UNSPECIFIED = ("application/vnd.dece.unspecified",)
    FILEFORMAT_APPLICATION_VND_DECE_ZIP = ("application/vnd.dece.zip",)
    FILEFORMAT_APPLICATION_VND_DENOVO_FCSELAYOUT_LINK = (
        "application/vnd.denovo.fcselayout-link",
    )
    FILEFORMAT_APPLICATION_VND_DESMUME_MOVIE = ("application/vnd.desmume.movie",)
    FILEFORMAT_APPLICATION_VND_DIR_BI_PLATE_DL_NOSUFFIX = (
        "application/vnd.dir-bi.plate-dl-nosuffix",
    )
    FILEFORMAT_APPLICATION_VND_DM_DELEGATION_XML = (
        "application/vnd.dm.delegation+xml",
    )
    FILEFORMAT_APPLICATION_VND_DNA = ("application/vnd.dna",)
    FILEFORMAT_APPLICATION_VND_DOCUMENT_JSON = ("application/vnd.document+json",)
    FILEFORMAT_APPLICATION_VND_DOLBY_MOBILE_1 = ("application/vnd.dolby.mobile.1",)
    FILEFORMAT_APPLICATION_VND_DOLBY_MOBILE_2 = ("application/vnd.dolby.mobile.2",)
    FILEFORMAT_APPLICATION_VND_DOREMIR_SCORECLOUD_BINARY_DOCUMENT = (
        "application/vnd.doremir.scorecloud-binary-document",
    )
    FILEFORMAT_APPLICATION_VND_DPGRAPH = ("application/vnd.dpgraph",)
    FILEFORMAT_APPLICATION_VND_DREAMFACTORY = ("application/vnd.dreamfactory",)
    FILEFORMAT_APPLICATION_VND_DRIVE_JSON = ("application/vnd.drive+json",)
    FILEFORMAT_APPLICATION_VND_DTG_LOCAL = ("application/vnd.dtg.local",)
    FILEFORMAT_APPLICATION_VND_DTG_LOCAL_FLASH = ("application/vnd.dtg.local.flash",)
    FILEFORMAT_APPLICATION_VND_DTG_LOCAL_HTML = ("application/vnd.dtg.local.html",)
    FILEFORMAT_APPLICATION_VND_DVB_AIT = ("application/vnd.dvb.ait",)
    FILEFORMAT_APPLICATION_VND_DVB_DVBJ = ("application/vnd.dvb.dvbj",)
    FILEFORMAT_APPLICATION_VND_DVB_ESGCONTAINER = ("application/vnd.dvb.esgcontainer",)
    FILEFORMAT_APPLICATION_VND_DVB_IPDCDFTNOTIFACCESS = (
        "application/vnd.dvb.ipdcdftnotifaccess",
    )
    FILEFORMAT_APPLICATION_VND_DVB_IPDCESGACCESS = (
        "application/vnd.dvb.ipdcesgaccess",
    )
    FILEFORMAT_APPLICATION_VND_DVB_IPDCESGACCESS2 = (
        "application/vnd.dvb.ipdcesgaccess2",
    )
    FILEFORMAT_APPLICATION_VND_DVB_IPDCESGPDD = ("application/vnd.dvb.ipdcesgpdd",)
    FILEFORMAT_APPLICATION_VND_DVB_IPDCROAMING = ("application/vnd.dvb.ipdcroaming",)
    FILEFORMAT_APPLICATION_VND_DVB_IPTV_ALFEC_BASE = (
        "application/vnd.dvb.iptv.alfec-base",
    )
    FILEFORMAT_APPLICATION_VND_DVB_IPTV_ALFEC_ENHANCEMENT = (
        "application/vnd.dvb.iptv.alfec-enhancement",
    )
    FILEFORMAT_APPLICATION_VND_DVB_NOTIF_AGGREGATE_ROOT_XML = (
        "application/vnd.dvb.notif-aggregate-root+xml",
    )
    FILEFORMAT_APPLICATION_VND_DVB_NOTIFCONTAINER_XML = (
        "application/vnd.dvb.notif-container+xml",
    )
    FILEFORMAT_APPLICATION_VND_DVB_NOTIF_GENERIC_XML = (
        "application/vnd.dvb.notif-generic+xml",
    )
    FILEFORMAT_APPLICATION_VND_DVB_NOTIF_IA_MSGLIST_XML = (
        "application/vnd.dvb.notif-ia-msglist+xml",
    )
    FILEFORMAT_APPLICATION_VND_DVB_NOTIF_IA_REGISTRATION_REQUEST_XML = (
        "application/vnd.dvb.notif-ia-registration-request+xml",
    )
    FILEFORMAT_APPLICATION_VND_DVB_NOTIF_IA_REGISTRATION_RESPONSE_XML = (
        "application/vnd.dvb.notif-ia-registration-response+xml",
    )
    FILEFORMAT_APPLICATION_VND_DVB_NOTIF_INIT_XML = (
        "application/vnd.dvb.notif-init+xml",
    )
    FILEFORMAT_APPLICATION_VND_DVB_PFR = ("application/vnd.dvb.pfr",)
    FILEFORMAT_APPLICATION_VND_DVB_SERVICE = ("application/vnd.dvb.service",)
    FILEFORMAT_APPLICATION_VND_DXR = ("application/vnd.dxr",)
    FILEFORMAT_APPLICATION_VND_DYNAGEO = ("application/vnd.dynageo",)
    FILEFORMAT_APPLICATION_VND_DZR = ("application/vnd.dzr",)
    FILEFORMAT_APPLICATION_VND_EASYKARAOKE_CDGDOWNLOAD = (
        "application/vnd.easykaraoke.cdgdownload",
    )
    FILEFORMAT_APPLICATION_VND_ECDIS_UPDATE = ("application/vnd.ecdis-update",)
    FILEFORMAT_APPLICATION_VND_ECOWIN_CHART = ("application/vnd.ecowin.chart",)
    FILEFORMAT_APPLICATION_VND_ECOWIN_FILEREQUEST = (
        "application/vnd.ecowin.filerequest",
    )
    FILEFORMAT_APPLICATION_VND_ECOWIN_FILEUPDATE = (
        "application/vnd.ecowin.fileupdate",
    )
    FILEFORMAT_APPLICATION_VND_ECOWIN_SERIES = ("application/vnd.ecowin.series",)
    FILEFORMAT_APPLICATION_VND_ECOWIN_SERIESREQUEST = (
        "application/vnd.ecowin.seriesrequest",
    )
    FILEFORMAT_APPLICATION_VND_ECOWIN_SERIESUPDATE = (
        "application/vnd.ecowin.seriesupdate",
    )
    FILEFORMAT_APPLICATION_VND_EFI_IMG = ("application/vnd.efi.img",)
    FILEFORMAT_APPLICATION_VND_EFI_ISO = ("application/vnd.efi.iso",)
    FILEFORMAT_APPLICATION_VND_EMCLIENT_ACCESSREQUEST_XML = (
        "application/vnd.emclient.accessrequest+xml",
    )
    FILEFORMAT_APPLICATION_VND_ENLIVEN = ("application/vnd.enliven",)
    FILEFORMAT_APPLICATION_VND_ENPHASE_ENVOY = ("application/vnd.enphase.envoy",)
    FILEFORMAT_APPLICATION_VND_EPRINTS_DATA_XML = ("application/vnd.eprints.data+xml",)
    FILEFORMAT_APPLICATION_VND_EPSON_ESF = ("application/vnd.epson.esf",)
    FILEFORMAT_APPLICATION_VND_EPSON_MSF = ("application/vnd.epson.msf",)
    FILEFORMAT_APPLICATION_VND_EPSON_QUICKANIME = ("application/vnd.epson.quickanime",)
    FILEFORMAT_APPLICATION_VND_EPSON_SALT = ("application/vnd.epson.salt",)
    FILEFORMAT_APPLICATION_VND_EPSON_SSF = ("application/vnd.epson.ssf",)
    FILEFORMAT_APPLICATION_VND_ERICSSON_QUICKCALL = (
        "application/vnd.ericsson.quickcall",
    )
    FILEFORMAT_APPLICATION_VND_ESPASS_ESPASS_ZIP = (
        "application/vnd.espass-espass+zip",
    )
    FILEFORMAT_APPLICATION_VND_ESZIGNO3_XML = ("application/vnd.eszigno3+xml",)
    FILEFORMAT_APPLICATION_VND_ETSI_AOC_XML = ("application/vnd.etsi.aoc+xml",)
    FILEFORMAT_APPLICATION_VND_ETSI_ASIC_S_ZIP = ("application/vnd.etsi.asic-s+zip",)
    FILEFORMAT_APPLICATION_VND_ETSI_ASIC_E_ZIP = ("application/vnd.etsi.asic-e+zip",)
    FILEFORMAT_APPLICATION_VND_ETSI_CUG_XML = ("application/vnd.etsi.cug+xml",)
    FILEFORMAT_APPLICATION_VND_ETSI_IPTVCOMMAND_XML = (
        "application/vnd.etsi.iptvcommand+xml",
    )
    FILEFORMAT_APPLICATION_VND_ETSI_IPTVDISCOVERY_XML = (
        "application/vnd.etsi.iptvdiscovery+xml",
    )
    FILEFORMAT_APPLICATION_VND_ETSI_IPTVPROFILE_XML = (
        "application/vnd.etsi.iptvprofile+xml",
    )
    FILEFORMAT_APPLICATION_VND_ETSI_IPTVSAD_BC_XML = (
        "application/vnd.etsi.iptvsad-bc+xml",
    )
    FILEFORMAT_APPLICATION_VND_ETSI_IPTVSADCOD_XML = (
        "application/vnd.etsi.iptvsad-cod+xml",
    )
    FILEFORMAT_APPLICATION_VND_ETSI_IPTVSAD_NPVR_XML = (
        "application/vnd.etsi.iptvsad-npvr+xml",
    )
    FILEFORMAT_APPLICATION_VND_ETSI_IPTVSERVICE_XML = (
        "application/vnd.etsi.iptvservice+xml",
    )
    FILEFORMAT_APPLICATION_VND_ETSI_IPTVSYNC_XML = (
        "application/vnd.etsi.iptvsync+xml",
    )
    FILEFORMAT_APPLICATION_VND_ETSI_IPTVUEPROFILE_XML = (
        "application/vnd.etsi.iptvueprofile+xml",
    )
    FILEFORMAT_APPLICATION_VND_ETSI_MCID_XML = ("application/vnd.etsi.mcid+xml",)
    FILEFORMAT_APPLICATION_VND_ETSI_MHEG5 = ("application/vnd.etsi.mheg5",)
    FILEFORMAT_APPLICATION_VND_ETSI_OVERLOADCONTROL_POLICY_DATASET_XML = (
        "application/vnd.etsi.overload-control-policy-dataset+xml",
    )
    FILEFORMAT_APPLICATION_VND_ETSI_PSTN_XML = ("application/vnd.etsi.pstn+xml",)
    FILEFORMAT_APPLICATION_VND_ETSI_SCI_XML = ("application/vnd.etsi.sci+xml",)
    FILEFORMAT_APPLICATION_VND_ETSI_SIMSERVS_XML = (
        "application/vnd.etsi.simservs+xml",
    )
    FILEFORMAT_APPLICATION_VND_ETSI_TIMESTAMP_TOKEN = (
        "application/vnd.etsi.timestamp-token",
    )
    FILEFORMAT_APPLICATION_VND_ETSI_TSL_XML = ("application/vnd.etsi.tsl+xml",)
    FILEFORMAT_APPLICATION_VND_ETSI_TSL_DER = ("application/vnd.etsi.tsl.der",)
    FILEFORMAT_APPLICATION_VND_EVOLV_ECIG_THEME = ("application/vnd.evolv.ecig.theme",)
    FILEFORMAT_APPLICATION_VND_EUDORA_DATA = ("application/vnd.eudora.data",)
    FILEFORMAT_APPLICATION_VND_EZPIX_ALBUM = ("application/vnd.ezpix-album",)
    FILEFORMAT_APPLICATION_VND_EZPIX_PACKAGE = ("application/vnd.ezpix-package",)
    FILEFORMAT_APPLICATION_VND_F_SECURE_MOBILE = ("application/vnd.f-secure.mobile",)
    FILEFORMAT_APPLICATION_VND_FASTCOPY_DISK_IMAGE = (
        "application/vnd.fastcopy-disk-image",
    )
    FILEFORMAT_APPLICATION_VND_FDF = ("application/vnd.fdf",)
    FILEFORMAT_APPLICATION_VND_FDSN_MSEED = ("application/vnd.fdsn.mseed",)
    FILEFORMAT_APPLICATION_VND_FDSN_SEED = ("application/vnd.fdsn.seed",)
    FILEFORMAT_APPLICATION_VND_FFSNS = ("application/vnd.ffsns",)
    FILEFORMAT_APPLICATION_VND_FILMIT_ZFC = ("application/vnd.filmit.zfc",)
    FILEFORMAT_APPLICATION_VND_FINTS = ("application/vnd.fints",)
    FILEFORMAT_APPLICATION_VND_FIREMONKEYS_CLOUDCELL = (
        "application/vnd.firemonkeys.cloudcell",
    )
    FILEFORMAT_APPLICATION_VND_FLOGRAPHIT = ("application/vnd.FloGraphIt",)
    FILEFORMAT_APPLICATION_VND_FLUXTIME_CLIP = ("application/vnd.fluxtime.clip",)
    FILEFORMAT_APPLICATION_VND_FONT_FONTFORGE_SFD = (
        "application/vnd.font-fontforge-sfd",
    )
    FILEFORMAT_APPLICATION_VND_FRAMEMAKER = ("application/vnd.framemaker",)
    FILEFORMAT_APPLICATION_VND_FROGANS_FNC = ("application/vnd.frogans.fnc",)
    FILEFORMAT_APPLICATION_VND_FROGANS_LTF = ("application/vnd.frogans.ltf",)
    FILEFORMAT_APPLICATION_VND_FSC_WEBLAUNCH = ("application/vnd.fsc.weblaunch",)
    FILEFORMAT_APPLICATION_VND_FUJITSU_OASYS = ("application/vnd.fujitsu.oasys",)
    FILEFORMAT_APPLICATION_VND_FUJITSU_OASYS2 = ("application/vnd.fujitsu.oasys2",)
    FILEFORMAT_APPLICATION_VND_FUJITSU_OASYS3 = ("application/vnd.fujitsu.oasys3",)
    FILEFORMAT_APPLICATION_VND_FUJITSU_OASYSGP = ("application/vnd.fujitsu.oasysgp",)
    FILEFORMAT_APPLICATION_VND_FUJITSU_OASYSPRS = ("application/vnd.fujitsu.oasysprs",)
    FILEFORMAT_APPLICATION_VND_FUJIXEROX_ART4 = ("application/vnd.fujixerox.ART4",)
    FILEFORMAT_APPLICATION_VND_FUJIXEROX_ART_EX = ("application/vnd.fujixerox.ART-EX",)
    FILEFORMAT_APPLICATION_VND_FUJIXEROX_DDD = ("application/vnd.fujixerox.ddd",)
    FILEFORMAT_APPLICATION_VND_FUJIXEROX_DOCUWORKS = (
        "application/vnd.fujixerox.docuworks",
    )
    FILEFORMAT_APPLICATION_VND_FUJIXEROX_DOCUWORKS_BINDER = (
        "application/vnd.fujixerox.docuworks.binder",
    )
    FILEFORMAT_APPLICATION_VND_FUJIXEROX_DOCUWORKS_CONTAINER = (
        "application/vnd.fujixerox.docuworks.container",
    )
    FILEFORMAT_APPLICATION_VND_FUJIXEROX_HBPL = ("application/vnd.fujixerox.HBPL",)
    FILEFORMAT_APPLICATION_VND_FUT_MISNET = ("application/vnd.fut-misnet",)
    FILEFORMAT_APPLICATION_VND_FUZZYSHEET = ("application/vnd.fuzzysheet",)
    FILEFORMAT_APPLICATION_VND_GENOMATIX_TUXEDO = ("application/vnd.genomatix.tuxedo",)
    FILEFORMAT_APPLICATION_VND_GEO_JSON = ("application/vnd.geo+json",)
    FILEFORMAT_APPLICATION_VND_GEOCUBE_XML = ("application/vnd.geocube+xml",)
    FILEFORMAT_APPLICATION_VND_GEOGEBRA_FILE = ("application/vnd.geogebra.file",)
    FILEFORMAT_APPLICATION_VND_GEOGEBRA_TOOL = ("application/vnd.geogebra.tool",)
    FILEFORMAT_APPLICATION_VND_GEOMETRY_EXPLORER = (
        "application/vnd.geometry-explorer",
    )
    FILEFORMAT_APPLICATION_VND_GEONEXT = ("application/vnd.geonext",)
    FILEFORMAT_APPLICATION_VND_GEOPLAN = ("application/vnd.geoplan",)
    FILEFORMAT_APPLICATION_VND_GEOSPACE = ("application/vnd.geospace",)
    FILEFORMAT_APPLICATION_VND_GERBER = ("application/vnd.gerber",)
    FILEFORMAT_APPLICATION_VND_GLOBALPLATFORM_CARDCONTENT_MGT = (
        "application/vnd.globalplatform.card-content-mgt",
    )
    FILEFORMAT_APPLICATION_VND_GLOBALPLATFORM_CARDCONTENT_MGT_RESPONSE = (
        "application/vnd.globalplatform.card-content-mgt-response",
    )
    FILEFORMAT_APPLICATION_VND_GMX = ("application/vnd.gmx",)
    FILEFORMAT_APPLICATION_VND_GOOGLE_EARTH_KML_XML = (
        "application/vnd.google-earth.kml+xml",
    )
    FILEFORMAT_APPLICATION_VND_GOOGLE_EARTH_KMZ = ("application/vnd.google-earth.kmz",)
    FILEFORMAT_APPLICATION_VND_GOV_SK_E_FORM_XML = (
        "application/vnd.gov.sk.e-form+xml",
    )
    FILEFORMAT_APPLICATION_VND_GOV_SK_E_FORM_ZIP = (
        "application/vnd.gov.sk.e-form+zip",
    )
    FILEFORMAT_APPLICATION_VND_GOV_SK_XMLDATACONTAINER_XML = (
        "application/vnd.gov.sk.xmldatacontainer+xml",
    )
    FILEFORMAT_APPLICATION_VND_GRAFEQ = ("application/vnd.grafeq",)
    FILEFORMAT_APPLICATION_VND_GRIDMP = ("application/vnd.gridmp",)
    FILEFORMAT_APPLICATION_VND_GROOVE_ACCOUNT = ("application/vnd.groove-account",)
    FILEFORMAT_APPLICATION_VND_GROOVE_HELP = ("application/vnd.groove-help",)
    FILEFORMAT_APPLICATION_VND_GROOVE_IDENTITY_MESSAGE = (
        "application/vnd.groove-identity-message",
    )
    FILEFORMAT_APPLICATION_VND_GROOVE_INJECTOR = ("application/vnd.groove-injector",)
    FILEFORMAT_APPLICATION_VND_GROOVE_TOOL_MESSAGE = (
        "application/vnd.groove-tool-message",
    )
    FILEFORMAT_APPLICATION_VND_GROOVE_TOOL_TEMPLATE = (
        "application/vnd.groove-tool-template",
    )
    FILEFORMAT_APPLICATION_VND_GROOVE_VCARD = ("application/vnd.groove-vcard",)
    FILEFORMAT_APPLICATION_VND_HAL_JSON = ("application/vnd.hal+json",)
    FILEFORMAT_APPLICATION_VND_HAL_XML = ("application/vnd.hal+xml",)
    FILEFORMAT_APPLICATION_VND_HANDHELD_ENTERTAINMENT_XML = (
        "application/vnd.HandHeld-Entertainment+xml",
    )
    FILEFORMAT_APPLICATION_VND_HBCI = ("application/vnd.hbci",)
    FILEFORMAT_APPLICATION_VND_HC_JSON = ("application/vnd.hc+json",)
    FILEFORMAT_APPLICATION_VND_HCL_BIREPORTS = ("application/vnd.hcl-bireports",)
    FILEFORMAT_APPLICATION_VND_HDT = ("application/vnd.hdt",)
    FILEFORMAT_APPLICATION_VND_HEROKU_JSON = ("application/vnd.heroku+json",)
    FILEFORMAT_APPLICATION_VND_HHE_LESSON_PLAYER = (
        "application/vnd.hhe.lesson-player",
    )
    FILEFORMAT_APPLICATION_VND_HP_HPGL = ("application/vnd.hp-HPGL",)
    FILEFORMAT_APPLICATION_VND_HP_HPID = ("application/vnd.hp-hpid",)
    FILEFORMAT_APPLICATION_VND_HP_HPS = ("application/vnd.hp-hps",)
    FILEFORMAT_APPLICATION_VND_HP_JLYT = ("application/vnd.hp-jlyt",)
    FILEFORMAT_APPLICATION_VND_HP_PCL = ("application/vnd.hp-PCL",)
    FILEFORMAT_APPLICATION_VND_HP_PCLXL = ("application/vnd.hp-PCLXL",)
    FILEFORMAT_APPLICATION_VND_HTTPHONE = ("application/vnd.httphone",)
    FILEFORMAT_APPLICATION_VND_HYDROSTATIX_SOF_DATA = (
        "application/vnd.hydrostatix.sof-data",
    )
    FILEFORMAT_APPLICATION_VND_HYPER_ITEM_JSON = ("application/vnd.hyper-item+json",)
    FILEFORMAT_APPLICATION_VND_HYPERDRIVE_JSON = ("application/vnd.hyperdrive+json",)
    FILEFORMAT_APPLICATION_VND_HZN_3DCROSSWORD = ("application/vnd.hzn-3d-crossword",)
    FILEFORMAT_APPLICATION_VND_IBM_AFPLINEDATA = ("application/vnd.ibm.afplinedata",)
    FILEFORMAT_APPLICATION_VND_IBM_ELECTRONIC_MEDIA = (
        "application/vnd.ibm.electronic-media",
    )
    FILEFORMAT_APPLICATION_VND_IBM_MINIPAY = ("application/vnd.ibm.MiniPay",)
    FILEFORMAT_APPLICATION_VND_IBM_MODCAP = ("application/vnd.ibm.modcap",)
    FILEFORMAT_APPLICATION_VND_IBM_RIGHTS_MANAGEMENT = (
        "application/vnd.ibm.rights-management",
    )
    FILEFORMAT_APPLICATION_VND_IBM_SECURECONTAINER = (
        "application/vnd.ibm.secure-container",
    )
    FILEFORMAT_APPLICATION_VND_ICCPROFILE = ("application/vnd.iccprofile",)
    FILEFORMAT_APPLICATION_VND_IEEE_1905 = ("application/vnd.ieee.1905",)
    FILEFORMAT_APPLICATION_VND_IGLOADER = ("application/vnd.igloader",)
    FILEFORMAT_APPLICATION_VND_IMAGEMETER_FOLDER_ZIP = (
        "application/vnd.imagemeter.folder+zip",
    )
    FILEFORMAT_APPLICATION_VND_IMAGEMETER_IMAGE_ZIP = (
        "application/vnd.imagemeter.image+zip",
    )
    FILEFORMAT_APPLICATION_VND_IMMERVISION_IVP = ("application/vnd.immervision-ivp",)
    FILEFORMAT_APPLICATION_VND_IMMERVISION_IVU = ("application/vnd.immervision-ivu",)
    FILEFORMAT_APPLICATION_VND_IMS_IMSCCV1P1 = ("application/vnd.ims.imsccv1p1",)
    FILEFORMAT_APPLICATION_VND_IMS_IMSCCV1P2 = ("application/vnd.ims.imsccv1p2",)
    FILEFORMAT_APPLICATION_VND_IMS_IMSCCV1P3 = ("application/vnd.ims.imsccv1p3",)
    FILEFORMAT_APPLICATION_VND_IMS_LIS_V2_RESULT_JSON = (
        "application/vnd.ims.lis.v2.result+json",
    )
    FILEFORMAT_APPLICATION_VND_IMS_LTI_V2_TOOLCONSUMERPROFILE_JSON = (
        "application/vnd.ims.lti.v2.toolconsumerprofile+json",
    )
    FILEFORMAT_APPLICATION_VND_IMS_LTI_V2_TOOLPROXY_ID_JSON = (
        "application/vnd.ims.lti.v2.toolproxy.id+json",
    )
    FILEFORMAT_APPLICATION_VND_IMS_LTI_V2_TOOLPROXY_JSON = (
        "application/vnd.ims.lti.v2.toolproxy+json",
    )
    FILEFORMAT_APPLICATION_VND_IMS_LTI_V2_TOOLSETTINGS_JSON = (
        "application/vnd.ims.lti.v2.toolsettings+json",
    )
    FILEFORMAT_APPLICATION_VND_IMS_LTI_V2_TOOLSETTINGS_SIMPLE_JSON = (
        "application/vnd.ims.lti.v2.toolsettings.simple+json",
    )
    FILEFORMAT_APPLICATION_VND_INFORMEDCONTROL_RMS_XML = (
        "application/vnd.informedcontrol.rms+xml",
    )
    FILEFORMAT_APPLICATION_VND_INFOTECH_PROJECT = ("application/vnd.infotech.project",)
    FILEFORMAT_APPLICATION_VND_INFOTECH_PROJECT_XML = (
        "application/vnd.infotech.project+xml",
    )
    FILEFORMAT_APPLICATION_VND_INFORMIX_VISIONARY = (
        "application/vnd.informix-visionary",
    )
    FILEFORMAT_APPLICATION_VND_INNOPATH_WAMP_NOTIFICATION = (
        "application/vnd.innopath.wamp.notification",
    )
    FILEFORMAT_APPLICATION_VND_INSORS_IGM = ("application/vnd.insors.igm",)
    FILEFORMAT_APPLICATION_VND_INTERCON_FORMNET = ("application/vnd.intercon.formnet",)
    FILEFORMAT_APPLICATION_VND_INTERGEO = ("application/vnd.intergeo",)
    FILEFORMAT_APPLICATION_VND_INTERTRUST_DIGIBOX = (
        "application/vnd.intertrust.digibox",
    )
    FILEFORMAT_APPLICATION_VND_INTERTRUST_NNCP = ("application/vnd.intertrust.nncp",)
    FILEFORMAT_APPLICATION_VND_INTU_QBO = ("application/vnd.intu.qbo",)
    FILEFORMAT_APPLICATION_VND_INTU_QFX = ("application/vnd.intu.qfx",)
    FILEFORMAT_APPLICATION_VND_IPTC_G2_CATALOGITEM_XML = (
        "application/vnd.iptc.g2.catalogitem+xml",
    )
    FILEFORMAT_APPLICATION_VND_IPTC_G2_CONCEPTITEM_XML = (
        "application/vnd.iptc.g2.conceptitem+xml",
    )
    FILEFORMAT_APPLICATION_VND_IPTC_G2_KNOWLEDGEITEM_XML = (
        "application/vnd.iptc.g2.knowledgeitem+xml",
    )
    FILEFORMAT_APPLICATION_VND_IPTC_G2_NEWSITEM_XML = (
        "application/vnd.iptc.g2.newsitem+xml",
    )
    FILEFORMAT_APPLICATION_VND_IPTC_G2_NEWSMESSAGE_XML = (
        "application/vnd.iptc.g2.newsmessage+xml",
    )
    FILEFORMAT_APPLICATION_VND_IPTC_G2_PACKAGEITEM_XML = (
        "application/vnd.iptc.g2.packageitem+xml",
    )
    FILEFORMAT_APPLICATION_VND_IPTC_G2_PLANNINGITEM_XML = (
        "application/vnd.iptc.g2.planningitem+xml",
    )
    FILEFORMAT_APPLICATION_VND_IPUNPLUGGED_RCPROFILE = (
        "application/vnd.ipunplugged.rcprofile",
    )
    FILEFORMAT_APPLICATION_VND_IREPOSITORY_PACKAGE_XML = (
        "application/vnd.irepository.package+xml",
    )
    FILEFORMAT_APPLICATION_VND_IS_XPR = ("application/vnd.is-xpr",)
    FILEFORMAT_APPLICATION_VND_ISAC_FCS = ("application/vnd.isac.fcs",)
    FILEFORMAT_APPLICATION_VND_JAM = ("application/vnd.jam",)
    FILEFORMAT_APPLICATION_VND_JAPANNET_DIRECTORY_SERVICE = (
        "application/vnd.japannet-directory-service",
    )
    FILEFORMAT_APPLICATION_VND_JAPANNET_JPNSTORE_WAKEUP = (
        "application/vnd.japannet-jpnstore-wakeup",
    )
    FILEFORMAT_APPLICATION_VND_JAPANNET_PAYMENT_WAKEUP = (
        "application/vnd.japannet-payment-wakeup",
    )
    FILEFORMAT_APPLICATION_VND_JAPANNET_REGISTRATION = (
        "application/vnd.japannet-registration",
    )
    FILEFORMAT_APPLICATION_VND_JAPANNET_REGISTRATION_WAKEUP = (
        "application/vnd.japannet-registration-wakeup",
    )
    FILEFORMAT_APPLICATION_VND_JAPANNET_SETSTORE_WAKEUP = (
        "application/vnd.japannet-setstore-wakeup",
    )
    FILEFORMAT_APPLICATION_VND_JAPANNET_VERIFICATION = (
        "application/vnd.japannet-verification",
    )
    FILEFORMAT_APPLICATION_VND_JAPANNET_VERIFICATION_WAKEUP = (
        "application/vnd.japannet-verification-wakeup",
    )
    FILEFORMAT_APPLICATION_VND_JCP_JAVAME_MIDLET_RMS = (
        "application/vnd.jcp.javame.midlet-rms",
    )
    FILEFORMAT_APPLICATION_VND_JISP = ("application/vnd.jisp",)
    FILEFORMAT_APPLICATION_VND_JOOST_JODA_ARCHIVE = (
        "application/vnd.joost.joda-archive",
    )
    FILEFORMAT_APPLICATION_VND_JSK_ISDN_NGN = ("application/vnd.jsk.isdn-ngn",)
    FILEFORMAT_APPLICATION_VND_KAHOOTZ = ("application/vnd.kahootz",)
    FILEFORMAT_APPLICATION_VND_KDE_KARBON = ("application/vnd.kde.karbon",)
    FILEFORMAT_APPLICATION_VND_KDE_KCHART = ("application/vnd.kde.kchart",)
    FILEFORMAT_APPLICATION_VND_KDE_KFORMULA = ("application/vnd.kde.kformula",)
    FILEFORMAT_APPLICATION_VND_KDE_KIVIO = ("application/vnd.kde.kivio",)
    FILEFORMAT_APPLICATION_VND_KDE_KONTOUR = ("application/vnd.kde.kontour",)
    FILEFORMAT_APPLICATION_VND_KDE_KPRESENTER = ("application/vnd.kde.kpresenter",)
    FILEFORMAT_APPLICATION_VND_KDE_KSPREAD = ("application/vnd.kde.kspread",)
    FILEFORMAT_APPLICATION_VND_KDE_KWORD = ("application/vnd.kde.kword",)
    FILEFORMAT_APPLICATION_VND_KENAMEAAPP = ("application/vnd.kenameaapp",)
    FILEFORMAT_APPLICATION_VND_KIDSPIRATION = ("application/vnd.kidspiration",)
    FILEFORMAT_APPLICATION_VND_KINAR = ("application/vnd.Kinar",)
    FILEFORMAT_APPLICATION_VND_KOAN = ("application/vnd.koan",)
    FILEFORMAT_APPLICATION_VND_KODAK_DESCRIPTOR = ("application/vnd.kodak-descriptor",)
    FILEFORMAT_APPLICATION_VND_LAS_LAS_JSON = ("application/vnd.las.las+json",)
    FILEFORMAT_APPLICATION_VND_LAS_LAS_XML = ("application/vnd.las.las+xml",)
    FILEFORMAT_APPLICATION_VND_LIBERTY_REQUEST_XML = (
        "application/vnd.liberty-request+xml",
    )
    FILEFORMAT_APPLICATION_VND_LLAMAGRAPHICS_LIFE_BALANCE_DESKTOP = (
        "application/vnd.llamagraphics.life-balance.desktop",
    )
    FILEFORMAT_APPLICATION_VND_LLAMAGRAPHICS_LIFE_BALANCE_EXCHANGE_XML = (
        "application/vnd.llamagraphics.life-balance.exchange+xml",
    )
    FILEFORMAT_APPLICATION_VND_LOTUS_1_2_3 = ("application/vnd.lotus-1-2-3",)
    FILEFORMAT_APPLICATION_VND_LOTUS_APPROACH = ("application/vnd.lotus-approach",)
    FILEFORMAT_APPLICATION_VND_LOTUS_FREELANCE = ("application/vnd.lotus-freelance",)
    FILEFORMAT_APPLICATION_VND_LOTUS_NOTES = ("application/vnd.lotus-notes",)
    FILEFORMAT_APPLICATION_VND_LOTUS_ORGANIZER = ("application/vnd.lotus-organizer",)
    FILEFORMAT_APPLICATION_VND_LOTUS_SCREENCAM = ("application/vnd.lotus-screencam",)
    FILEFORMAT_APPLICATION_VND_LOTUS_WORDPRO = ("application/vnd.lotus-wordpro",)
    FILEFORMAT_APPLICATION_VND_MACPORTS_PORTPKG = ("application/vnd.macports.portpkg",)
    FILEFORMAT_APPLICATION_VND_MACPORTS_PORTPKG = ("application/vnd.macports.portpkg",)
    FILEFORMAT_APPLICATION_VND_MAPBOX_VECTOR_TILE = (
        "application/vnd.mapbox-vector-tile",
    )
    FILEFORMAT_APPLICATION_VND_MARLIN_DRM_ACTIONTOKEN_XML = (
        "application/vnd.marlin.drm.actiontoken+xml",
    )
    FILEFORMAT_APPLICATION_VND_MARLIN_DRM_CONFTOKEN_XML = (
        "application/vnd.marlin.drm.conftoken+xml",
    )
    FILEFORMAT_APPLICATION_VND_MARLIN_DRM_LICENSE_XML = (
        "application/vnd.marlin.drm.license+xml",
    )
    FILEFORMAT_APPLICATION_VND_MARLIN_DRM_MDCF = ("application/vnd.marlin.drm.mdcf",)
    FILEFORMAT_APPLICATION_VND_MASON_JSON = ("application/vnd.mason+json",)
    FILEFORMAT_APPLICATION_VND_MAXMIND_MAXMIND_DB = (
        "application/vnd.maxmind.maxmind-db",
    )
    FILEFORMAT_APPLICATION_VND_MCD = ("application/vnd.mcd",)
    FILEFORMAT_APPLICATION_VND_MEDCALCDATA = ("application/vnd.medcalcdata",)
    FILEFORMAT_APPLICATION_VND_MEDIASTATION_CDKEY = (
        "application/vnd.mediastation.cdkey",
    )
    FILEFORMAT_APPLICATION_VND_MERIDIAN_SLINGSHOT = (
        "application/vnd.meridian-slingshot",
    )
    FILEFORMAT_APPLICATION_VND_MFER = ("application/vnd.MFER",)
    FILEFORMAT_APPLICATION_VND_MFMP = ("application/vnd.mfmp",)
    FILEFORMAT_APPLICATION_VND_MICRO_JSON = ("application/vnd.micro+json",)
    FILEFORMAT_APPLICATION_VND_MICROGRAFX_FLO = ("application/vnd.micrografx.flo",)
    FILEFORMAT_APPLICATION_VND_MICROGRAFX_IGX = ("application/vnd.micrografx.igx",)
    FILEFORMAT_APPLICATION_VND_MICROSOFT_PORTABLE_EXECUTABLE = (
        "application/vnd.microsoft.portable-executable",
    )
    FILEFORMAT_APPLICATION_VND_MICROSOFT_WINDOWS_THUMBNAILCACHE = (
        "application/vnd.microsoft.windows.thumbnail-cache",
    )
    FILEFORMAT_APPLICATION_VND_MIELE_JSON = ("application/vnd.miele+json",)
    FILEFORMAT_APPLICATION_VND_MIF = ("application/vnd.mif",)
    FILEFORMAT_APPLICATION_VND_MINISOFT_HP3000_SAVE = (
        "application/vnd.minisoft-hp3000-save",
    )
    FILEFORMAT_APPLICATION_VND_MITSUBISHI_MISTY_GUARD_TRUSTWEB = (
        "application/vnd.mitsubishi.misty-guard.trustweb",
    )
    FILEFORMAT_APPLICATION_VND_MOBIUS_DAF = ("application/vnd.Mobius.DAF",)
    FILEFORMAT_APPLICATION_VND_MOBIUS_DIS = ("application/vnd.Mobius.DIS",)
    FILEFORMAT_APPLICATION_VND_MOBIUS_MBK = ("application/vnd.Mobius.MBK",)
    FILEFORMAT_APPLICATION_VND_MOBIUS_MQY = ("application/vnd.Mobius.MQY",)
    FILEFORMAT_APPLICATION_VND_MOBIUS_MSL = ("application/vnd.Mobius.MSL",)
    FILEFORMAT_APPLICATION_VND_MOBIUS_PLC = ("application/vnd.Mobius.PLC",)
    FILEFORMAT_APPLICATION_VND_MOBIUS_TXF = ("application/vnd.Mobius.TXF",)
    FILEFORMAT_APPLICATION_VND_MOPHUN_APPLICATION = (
        "application/vnd.mophun.application",
    )
    FILEFORMAT_APPLICATION_VND_MOPHUN_CERTIFICATE = (
        "application/vnd.mophun.certificate",
    )
    FILEFORMAT_APPLICATION_VND_MOTOROLA_FLEXSUITE = (
        "application/vnd.motorola.flexsuite",
    )
    FILEFORMAT_APPLICATION_VND_MOTOROLA_FLEXSUITE_ADSI = (
        "application/vnd.motorola.flexsuite.adsi",
    )
    FILEFORMAT_APPLICATION_VND_MOTOROLA_FLEXSUITE_FIS = (
        "application/vnd.motorola.flexsuite.fis",
    )
    FILEFORMAT_APPLICATION_VND_MOTOROLA_FLEXSUITE_GOTAP = (
        "application/vnd.motorola.flexsuite.gotap",
    )
    FILEFORMAT_APPLICATION_VND_MOTOROLA_FLEXSUITE_KMR = (
        "application/vnd.motorola.flexsuite.kmr",
    )
    FILEFORMAT_APPLICATION_VND_MOTOROLA_FLEXSUITE_TTC = (
        "application/vnd.motorola.flexsuite.ttc",
    )
    FILEFORMAT_APPLICATION_VND_MOTOROLA_FLEXSUITE_WEM = (
        "application/vnd.motorola.flexsuite.wem",
    )
    FILEFORMAT_APPLICATION_VND_MOTOROLA_IPRM = ("application/vnd.motorola.iprm",)
    FILEFORMAT_APPLICATION_VND_MOZILLA_XUL_XML = ("application/vnd.mozilla.xul+xml",)
    FILEFORMAT_APPLICATION_VND_MS_ARTGALRY = ("application/vnd.ms-artgalry",)
    FILEFORMAT_APPLICATION_VND_MS_ASF = ("application/vnd.ms-asf",)
    FILEFORMAT_APPLICATION_VND_MSCABCOMPRESSED = ("application/vnd.ms-cab-compressed",)
    FILEFORMAT_APPLICATION_VND_MS_3MFDOCUMENT = ("application/vnd.ms-3mfdocument",)
    FILEFORMAT_APPLICATION_VND_MS_EXCEL = ("application/vnd.ms-excel",)
    FILEFORMAT_APPLICATION_VND_MS_EXCEL_ADDIN_MACROENABLED_12 = (
        "application/vnd.ms-excel.addin.macroEnabled.12",
    )
    FILEFORMAT_APPLICATION_VND_MS_EXCEL_SHEET_BINARY_MACROENABLED_12 = (
        "application/vnd.ms-excel.sheet.binary.macroEnabled.12",
    )
    FILEFORMAT_APPLICATION_VND_MS_EXCEL_SHEET_MACROENABLED_12 = (
        "application/vnd.ms-excel.sheet.macroEnabled.12",
    )
    FILEFORMAT_APPLICATION_VND_MS_EXCEL_TEMPLATE_MACROENABLED_12 = (
        "application/vnd.ms-excel.template.macroEnabled.12",
    )
    FILEFORMAT_APPLICATION_VND_MS_FONTOBJECT = ("application/vnd.ms-fontobject",)
    FILEFORMAT_APPLICATION_VND_MS_HTMLHELP = ("application/vnd.ms-htmlhelp",)
    FILEFORMAT_APPLICATION_VND_MS_IMS = ("application/vnd.ms-ims",)
    FILEFORMAT_APPLICATION_VND_MS_LRM = ("application/vnd.ms-lrm",)
    FILEFORMAT_APPLICATION_VND_MS_OFFICE_ACTIVEX_XML = (
        "application/vnd.ms-office.activeX+xml",
    )
    FILEFORMAT_APPLICATION_VND_MS_OFFICETHEME = ("application/vnd.ms-officetheme",)
    FILEFORMAT_APPLICATION_VND_MS_PLAYREADY_INITIATOR_XML = (
        "application/vnd.ms-playready.initiator+xml",
    )
    FILEFORMAT_APPLICATION_VND_MS_POWERPOINT = ("application/vnd.ms-powerpoint",)
    FILEFORMAT_APPLICATION_VND_MS_POWERPOINT_ADDIN_MACROENABLED_12 = (
        "application/vnd.ms-powerpoint.addin.macroEnabled.12",
    )
    FILEFORMAT_APPLICATION_VND_MS_POWERPOINT_PRESENTATION_MACROENABLED_12 = (
        "application/vnd.ms-powerpoint.presentation.macroEnabled.12",
    )
    FILEFORMAT_APPLICATION_VND_MS_POWERPOINT_SLIDE_MACROENABLED_12 = (
        "application/vnd.ms-powerpoint.slide.macroEnabled.12",
    )
    FILEFORMAT_APPLICATION_VND_MS_POWERPOINT_SLIDESHOW_MACROENABLED_12 = (
        "application/vnd.ms-powerpoint.slideshow.macroEnabled.12",
    )
    FILEFORMAT_APPLICATION_VND_MS_POWERPOINT_TEMPLATE_MACROENABLED_12 = (
        "application/vnd.ms-powerpoint.template.macroEnabled.12",
    )
    FILEFORMAT_APPLICATION_VND_MS_PRINTDEVICECAPABILITIES_XML = (
        "application/vnd.ms-PrintDeviceCapabilities+xml",
    )
    FILEFORMAT_APPLICATION_VND_MS_PRINTSCHEMATICKET_XML = (
        "application/vnd.ms-PrintSchemaTicket+xml",
    )
    FILEFORMAT_APPLICATION_VND_MS_PROJECT = ("application/vnd.ms-project",)
    FILEFORMAT_APPLICATION_VND_MS_TNEF = ("application/vnd.ms-tnef",)
    FILEFORMAT_APPLICATION_VND_MS_WINDOWS_DEVICEPAIRING = (
        "application/vnd.ms-windows.devicepairing",
    )
    FILEFORMAT_APPLICATION_VND_MS_WINDOWS_NWPRINTING_OOB = (
        "application/vnd.ms-windows.nwprinting.oob",
    )
    FILEFORMAT_APPLICATION_VND_MS_WINDOWS_PRINTERPAIRING = (
        "application/vnd.ms-windows.printerpairing",
    )
    FILEFORMAT_APPLICATION_VND_MS_WINDOWS_WSD_OOB = (
        "application/vnd.ms-windows.wsd.oob",
    )
    FILEFORMAT_APPLICATION_VND_MS_WMDRM_LICCHLG_REQ = (
        "application/vnd.ms-wmdrm.lic-chlg-req",
    )
    FILEFORMAT_APPLICATION_VND_MS_WMDRM_LIC_RESP = (
        "application/vnd.ms-wmdrm.lic-resp",
    )
    FILEFORMAT_APPLICATION_VND_MS_WMDRM_METERCHLG_REQ = (
        "application/vnd.ms-wmdrm.meter-chlg-req",
    )
    FILEFORMAT_APPLICATION_VND_MS_WMDRM_METER_RESP = (
        "application/vnd.ms-wmdrm.meter-resp",
    )
    FILEFORMAT_APPLICATION_VND_MS_WORD_DOCUMENT_MACROENABLED_12 = (
        "application/vnd.ms-word.document.macroEnabled.12",
    )
    FILEFORMAT_APPLICATION_VND_MS_WORD_TEMPLATE_MACROENABLED_12 = (
        "application/vnd.ms-word.template.macroEnabled.12",
    )
    FILEFORMAT_APPLICATION_VND_MS_WORKS = ("application/vnd.ms-works",)
    FILEFORMAT_APPLICATION_VND_MS_WPL = ("application/vnd.ms-wpl",)
    FILEFORMAT_APPLICATION_VND_MS_XPSDOCUMENT = ("application/vnd.ms-xpsdocument",)
    FILEFORMAT_APPLICATION_VND_MSA_DISK_IMAGE = ("application/vnd.msa-disk-image",)
    FILEFORMAT_APPLICATION_VND_MSEQ = ("application/vnd.mseq",)
    FILEFORMAT_APPLICATION_VND_MSIGN = ("application/vnd.msign",)
    FILEFORMAT_APPLICATION_VND_MULTIAD_CREATOR = ("application/vnd.multiad.creator",)
    FILEFORMAT_APPLICATION_VND_MULTIAD_CREATOR_CIF = (
        "application/vnd.multiad.creator.cif",
    )
    FILEFORMAT_APPLICATION_VND_MUSICIAN = ("application/vnd.musician",)
    FILEFORMAT_APPLICATION_VND_MUSIC_NIFF = ("application/vnd.music-niff",)
    FILEFORMAT_APPLICATION_VND_MUVEE_STYLE = ("application/vnd.muvee.style",)
    FILEFORMAT_APPLICATION_VND_MYNFC = ("application/vnd.mynfc",)
    FILEFORMAT_APPLICATION_VND_NCD_CONTROL = ("application/vnd.ncd.control",)
    FILEFORMAT_APPLICATION_VND_NCD_REFERENCE = ("application/vnd.ncd.reference",)
    FILEFORMAT_APPLICATION_VND_NEARST_INV_JSON = ("application/vnd.nearst.inv+json",)
    FILEFORMAT_APPLICATION_VND_NERVANA = ("application/vnd.nervana",)
    FILEFORMAT_APPLICATION_VND_NETFPX = ("application/vnd.netfpx",)
    FILEFORMAT_APPLICATION_VND_NEUROLANGUAGE_NLU = (
        "application/vnd.neurolanguage.nlu",
    )
    FILEFORMAT_APPLICATION_VND_NINTENDO_SNES_ROM = (
        "application/vnd.nintendo.snes.rom",
    )
    FILEFORMAT_APPLICATION_VND_NINTENDO_NITRO_ROM = (
        "application/vnd.nintendo.nitro.rom",
    )
    FILEFORMAT_APPLICATION_VND_NITF = ("application/vnd.nitf",)
    FILEFORMAT_APPLICATION_VND_NOBLENET_DIRECTORY = (
        "application/vnd.noblenet-directory",
    )
    FILEFORMAT_APPLICATION_VND_NOBLENET_SEALER = ("application/vnd.noblenet-sealer",)
    FILEFORMAT_APPLICATION_VND_NOBLENET_WEB = ("application/vnd.noblenet-web",)
    FILEFORMAT_APPLICATION_VND_NOKIA_CATALOGS = ("application/vnd.nokia.catalogs",)
    FILEFORMAT_APPLICATION_VND_NOKIA_CONML_WBXML = (
        "application/vnd.nokia.conml+wbxml",
    )
    FILEFORMAT_APPLICATION_VND_NOKIA_CONML_XML = ("application/vnd.nokia.conml+xml",)
    FILEFORMAT_APPLICATION_VND_NOKIA_IPTV_CONFIG_XML = (
        "application/vnd.nokia.iptv.config+xml",
    )
    FILEFORMAT_APPLICATION_VND_NOKIA_ISDS_RADIO_PRESETS = (
        "application/vnd.nokia.iSDS-radio-presets",
    )
    FILEFORMAT_APPLICATION_VND_NOKIA_LANDMARK_WBXML = (
        "application/vnd.nokia.landmark+wbxml",
    )
    FILEFORMAT_APPLICATION_VND_NOKIA_LANDMARK_XML = (
        "application/vnd.nokia.landmark+xml",
    )
    FILEFORMAT_APPLICATION_VND_NOKIA_LANDMARKCOLLECTION_XML = (
        "application/vnd.nokia.landmarkcollection+xml",
    )
    FILEFORMAT_APPLICATION_VND_NOKIA_NCD = ("application/vnd.nokia.ncd",)
    FILEFORMAT_APPLICATION_VND_NOKIA_N_GAGE_AC_XML = (
        "application/vnd.nokia.n-gage.ac+xml",
    )
    FILEFORMAT_APPLICATION_VND_NOKIA_N_GAGE_DATA = (
        "application/vnd.nokia.n-gage.data",
    )
    FILEFORMAT_APPLICATION_VND_NOKIA_N_GAGE_SYMBIAN_INSTALL = (
        "application/vnd.nokia.n-gage.symbian.install",
    )
    FILEFORMAT_APPLICATION_VND_NOKIA_PCD_WBXML = ("application/vnd.nokia.pcd+wbxml",)
    FILEFORMAT_APPLICATION_VND_NOKIA_PCD_XML = ("application/vnd.nokia.pcd+xml",)
    FILEFORMAT_APPLICATION_VND_NOKIA_RADIO_PRESET = (
        "application/vnd.nokia.radio-preset",
    )
    FILEFORMAT_APPLICATION_VND_NOKIA_RADIO_PRESETS = (
        "application/vnd.nokia.radio-presets",
    )
    FILEFORMAT_APPLICATION_VND_NOVADIGM_EDM = ("application/vnd.novadigm.EDM",)
    FILEFORMAT_APPLICATION_VND_NOVADIGM_EDX = ("application/vnd.novadigm.EDX",)
    FILEFORMAT_APPLICATION_VND_NOVADIGM_EXT = ("application/vnd.novadigm.EXT",)
    FILEFORMAT_APPLICATION_VND_NTT_LOCAL_CONTENT_SHARE = (
        "application/vnd.ntt-local.content-share",
    )
    FILEFORMAT_APPLICATION_VND_NTT_LOCAL_FILE_TRANSFER = (
        "application/vnd.ntt-local.file-transfer",
    )
    FILEFORMAT_APPLICATION_VND_NTT_LOCAL_OGW_REMOTE_ACCESS = (
        "application/vnd.ntt-local.ogw_remote-access",
    )
    FILEFORMAT_APPLICATION_VND_NTT_LOCAL_SIP_TA_REMOTE = (
        "application/vnd.ntt-local.sip-ta_remote",
    )
    FILEFORMAT_APPLICATION_VND_NTT_LOCAL_SIP_TA_TCP_STREAM = (
        "application/vnd.ntt-local.sip-ta_tcp_stream",
    )
    FILEFORMAT_APPLICATION_VND_OASIS_OPENDOCUMENT_CHART = (
        "application/vnd.oasis.opendocument.chart",
    )
    FILEFORMAT_APPLICATION_VND_OASIS_OPENDOCUMENT_CHART_TEMPLATE = (
        "application/vnd.oasis.opendocument.chart-template",
    )
    FILEFORMAT_APPLICATION_VND_OASIS_OPENDOCUMENT_DATABASE = (
        "application/vnd.oasis.opendocument.database",
    )
    FILEFORMAT_APPLICATION_VND_OASIS_OPENDOCUMENT_FORMULA = (
        "application/vnd.oasis.opendocument.formula",
    )
    FILEFORMAT_APPLICATION_VND_OASIS_OPENDOCUMENT_FORMULA_TEMPLATE = (
        "application/vnd.oasis.opendocument.formula-template",
    )
    FILEFORMAT_APPLICATION_VND_OASIS_OPENDOCUMENT_GRAPHICS = (
        "application/vnd.oasis.opendocument.graphics",
    )
    FILEFORMAT_APPLICATION_VND_OASIS_OPENDOCUMENT_GRAPHICS_TEMPLATE = (
        "application/vnd.oasis.opendocument.graphics-template",
    )
    FILEFORMAT_APPLICATION_VND_OASIS_OPENDOCUMENT_IMAGE = (
        "application/vnd.oasis.opendocument.image",
    )
    FILEFORMAT_APPLICATION_VND_OASIS_OPENDOCUMENT_IMAGE_TEMPLATE = (
        "application/vnd.oasis.opendocument.image-template",
    )
    FILEFORMAT_APPLICATION_VND_OASIS_OPENDOCUMENT_PRESENTATION = (
        "application/vnd.oasis.opendocument.presentation",
    )
    FILEFORMAT_APPLICATION_VND_OASIS_OPENDOCUMENT_PRESENTATION_TEMPLATE = (
        "application/vnd.oasis.opendocument.presentation-template",
    )
    FILEFORMAT_APPLICATION_VND_OASIS_OPENDOCUMENT_SPREADSHEET = (
        "application/vnd.oasis.opendocument.spreadsheet",
    )
    FILEFORMAT_APPLICATION_VND_OASIS_OPENDOCUMENT_SPREADSHEET_TEMPLATE = (
        "application/vnd.oasis.opendocument.spreadsheet-template",
    )
    FILEFORMAT_APPLICATION_VND_OASIS_OPENDOCUMENT_TEXT = (
        "application/vnd.oasis.opendocument.text",
    )
    FILEFORMAT_APPLICATION_VND_OASIS_OPENDOCUMENT_TEXT_MASTER = (
        "application/vnd.oasis.opendocument.text-master",
    )
    FILEFORMAT_APPLICATION_VND_OASIS_OPENDOCUMENT_TEXT_TEMPLATE = (
        "application/vnd.oasis.opendocument.text-template",
    )
    FILEFORMAT_APPLICATION_VND_OASIS_OPENDOCUMENT_TEXT_WEB = (
        "application/vnd.oasis.opendocument.text-web",
    )
    FILEFORMAT_APPLICATION_VND_OBN = ("application/vnd.obn",)
    FILEFORMAT_APPLICATION_VND_OCF_CBOR = ("application/vnd.ocf+cbor",)
    FILEFORMAT_APPLICATION_VND_OFTN_L10N_JSON = ("application/vnd.oftn.l10n+json",)
    FILEFORMAT_APPLICATION_VND_OIPF_CONTENTACCESSDOWNLOAD_XML = (
        "application/vnd.oipf.contentaccessdownload+xml",
    )
    FILEFORMAT_APPLICATION_VND_OIPF_CONTENTACCESSSTREAMING_XML = (
        "application/vnd.oipf.contentaccessstreaming+xml",
    )
    FILEFORMAT_APPLICATION_VND_OIPF_CSPG_HEXBINARY = (
        "application/vnd.oipf.cspg-hexbinary",
    )
    FILEFORMAT_APPLICATION_VND_OIPF_DAE_SVG_XML = ("application/vnd.oipf.dae.svg+xml",)
    FILEFORMAT_APPLICATION_VND_OIPF_DAE_XHTML_XML = (
        "application/vnd.oipf.dae.xhtml+xml",
    )
    FILEFORMAT_APPLICATION_VND_OIPF_MIPPVCONTROLMESSAGE_XML = (
        "application/vnd.oipf.mippvcontrolmessage+xml",
    )
    FILEFORMAT_APPLICATION_VND_OIPF_PAE_GEM = ("application/vnd.oipf.pae.gem",)
    FILEFORMAT_APPLICATION_VND_OIPF_SPDISCOVERY_XML = (
        "application/vnd.oipf.spdiscovery+xml",
    )
    FILEFORMAT_APPLICATION_VND_OIPF_SPDLIST_XML = ("application/vnd.oipf.spdlist+xml",)
    FILEFORMAT_APPLICATION_VND_OIPF_UEPROFILE_XML = (
        "application/vnd.oipf.ueprofile+xml",
    )
    FILEFORMAT_APPLICATION_VND_OIPF_USERPROFILE_XML = (
        "application/vnd.oipf.userprofile+xml",
    )
    FILEFORMAT_APPLICATION_VND_OLPC_SUGAR = ("application/vnd.olpc-sugar",)
    FILEFORMAT_APPLICATION_VND_OMA_BCAST_ASSOCIATED_PROCEDURE_PARAMETER_XML = (
        "application/vnd.oma.bcast.associated-procedure-parameter+xml",
    )
    FILEFORMAT_APPLICATION_VND_OMA_BCAST_DRM_TRIGGER_XML = (
        "application/vnd.oma.bcast.drm-trigger+xml",
    )
    FILEFORMAT_APPLICATION_VND_OMA_BCAST_IMD_XML = (
        "application/vnd.oma.bcast.imd+xml",
    )
    FILEFORMAT_APPLICATION_VND_OMA_BCAST_LTKM = ("application/vnd.oma.bcast.ltkm",)
    FILEFORMAT_APPLICATION_VND_OMA_BCAST_NOTIFICATION_XML = (
        "application/vnd.oma.bcast.notification+xml",
    )
    FILEFORMAT_APPLICATION_VND_OMA_BCAST_PROVISIONINGTRIGGER = (
        "application/vnd.oma.bcast.provisioningtrigger",
    )
    FILEFORMAT_APPLICATION_VND_OMA_BCAST_SGBOOT = ("application/vnd.oma.bcast.sgboot",)
    FILEFORMAT_APPLICATION_VND_OMA_BCAST_SGDD_XML = (
        "application/vnd.oma.bcast.sgdd+xml",
    )
    FILEFORMAT_APPLICATION_VND_OMA_BCAST_SGDU = ("application/vnd.oma.bcast.sgdu",)
    FILEFORMAT_APPLICATION_VND_OMA_BCAST_SIMPLE_SYMBOLCONTAINER = (
        "application/vnd.oma.bcast.simple-symbol-container",
    )
    FILEFORMAT_APPLICATION_VND_OMA_BCAST_SMARTCARD_TRIGGER_XML = (
        "application/vnd.oma.bcast.smartcard-trigger+xml",
    )
    FILEFORMAT_APPLICATION_VND_OMA_BCAST_SPROV_XML = (
        "application/vnd.oma.bcast.sprov+xml",
    )
    FILEFORMAT_APPLICATION_VND_OMA_BCAST_STKM = ("application/vnd.oma.bcast.stkm",)
    FILEFORMAT_APPLICATION_VND_OMA_CAB_ADDRESS_BOOK_XML = (
        "application/vnd.oma.cab-address-book+xml",
    )
    FILEFORMAT_APPLICATION_VND_OMA_CAB_FEATURE_HANDLER_XML = (
        "application/vnd.oma.cab-feature-handler+xml",
    )
    FILEFORMAT_APPLICATION_VND_OMA_CAB_PCC_XML = ("application/vnd.oma.cab-pcc+xml",)
    FILEFORMAT_APPLICATION_VND_OMA_CAB_SUBS_INVITE_XML = (
        "application/vnd.oma.cab-subs-invite+xml",
    )
    FILEFORMAT_APPLICATION_VND_OMA_CAB_USER_PREFS_XML = (
        "application/vnd.oma.cab-user-prefs+xml",
    )
    FILEFORMAT_APPLICATION_VND_OMA_DCD = ("application/vnd.oma.dcd",)
    FILEFORMAT_APPLICATION_VND_OMA_DCDC = ("application/vnd.oma.dcdc",)
    FILEFORMAT_APPLICATION_VND_OMA_DD2_XML = ("application/vnd.oma.dd2+xml",)
    FILEFORMAT_APPLICATION_VND_OMA_DRM_RISD_XML = ("application/vnd.oma.drm.risd+xml",)
    FILEFORMAT_APPLICATION_VND_OMA_GROUP_USAGE_LIST_XML = (
        "application/vnd.oma.group-usage-list+xml",
    )
    FILEFORMAT_APPLICATION_VND_OMA_LWM2M_JSON = ("application/vnd.oma.lwm2m+json",)
    FILEFORMAT_APPLICATION_VND_OMA_LWM2M_TLV = ("application/vnd.oma.lwm2m+tlv",)
    FILEFORMAT_APPLICATION_VND_OMA_PAL_XML = ("application/vnd.oma.pal+xml",)
    FILEFORMAT_APPLICATION_VND_OMA_POC_DETAILED_PROGRESS_REPORT_XML = (
        "application/vnd.oma.poc.detailed-progress-report+xml",
    )
    FILEFORMAT_APPLICATION_VND_OMA_POC_FINAL_REPORT_XML = (
        "application/vnd.oma.poc.final-report+xml",
    )
    FILEFORMAT_APPLICATION_VND_OMA_POC_GROUPS_XML = (
        "application/vnd.oma.poc.groups+xml",
    )
    FILEFORMAT_APPLICATION_VND_OMA_POC_INVOCATION_DESCRIPTOR_XML = (
        "application/vnd.oma.poc.invocation-descriptor+xml",
    )
    FILEFORMAT_APPLICATION_VND_OMA_POC_OPTIMIZED_PROGRESS_REPORT_XML = (
        "application/vnd.oma.poc.optimized-progress-report+xml",
    )
    FILEFORMAT_APPLICATION_VND_OMA_PUSH = ("application/vnd.oma.push",)
    FILEFORMAT_APPLICATION_VND_OMA_SCIDM_MESSAGES_XML = (
        "application/vnd.oma.scidm.messages+xml",
    )
    FILEFORMAT_APPLICATION_VND_OMA_XCAP_DIRECTORY_XML = (
        "application/vnd.oma.xcap-directory+xml",
    )
    FILEFORMAT_APPLICATION_VND_OMADS_EMAIL_XML = ("application/vnd.omads-email+xml",)
    FILEFORMAT_APPLICATION_VND_OMADS_FILE_XML = ("application/vnd.omads-file+xml",)
    FILEFORMAT_APPLICATION_VND_OMADS_FOLDER_XML = ("application/vnd.omads-folder+xml",)
    FILEFORMAT_APPLICATION_VND_OMALOC_SUPL_INIT = ("application/vnd.omaloc-supl-init",)
    FILEFORMAT_APPLICATION_VND_OMA_SCWSCONFIG = ("application/vnd.oma-scws-config",)
    FILEFORMAT_APPLICATION_VND_OMA_SCWS_HTTP_REQUEST = (
        "application/vnd.oma-scws-http-request",
    )
    FILEFORMAT_APPLICATION_VND_OMA_SCWS_HTTP_RESPONSE = (
        "application/vnd.oma-scws-http-response",
    )
    FILEFORMAT_APPLICATION_VND_ONEPAGER = ("application/vnd.onepager",)
    FILEFORMAT_APPLICATION_VND_ONEPAGERTAMP = ("application/vnd.onepagertamp",)
    FILEFORMAT_APPLICATION_VND_ONEPAGERTAMX = ("application/vnd.onepagertamx",)
    FILEFORMAT_APPLICATION_VND_ONEPAGERTAT = ("application/vnd.onepagertat",)
    FILEFORMAT_APPLICATION_VND_ONEPAGERTATP = ("application/vnd.onepagertatp",)
    FILEFORMAT_APPLICATION_VND_ONEPAGERTATX = ("application/vnd.onepagertatx",)
    FILEFORMAT_APPLICATION_VND_OPENBLOX_GAME_BINARY = (
        "application/vnd.openblox.game-binary",
    )
    FILEFORMAT_APPLICATION_VND_OPENBLOX_GAME_XML = (
        "application/vnd.openblox.game+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENEYE_OEB = ("application/vnd.openeye.oeb",)
    FILEFORMAT_APPLICATION_VND_OPENSTREETMAP_DATA_XML = (
        "application/vnd.openstreetmap.data+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_CUSTOM_PROPERTIES_XML = (
        "application/vnd.openxmlformats-officedocument.custom-properties+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_CUSTOMXMLPROPERTIES_XML = (
        "application/vnd.openxmlformats-officedocument.customXmlProperties+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_DRAWING_XML = (
        "application/vnd.openxmlformats-officedocument.drawing+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_DRAWINGML_CHART_XML = (
        "application/vnd.openxmlformats-officedocument.drawingml.chart+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_DRAWINGML_CHARTSHAPES_XML = (
        "application/vnd.openxmlformats-officedocument.drawingml.chartshapes+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_DRAWINGML_DIAGRAMCOLORS_XML = (
        "application/vnd.openxmlformats-officedocument.drawingml.diagramColors+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_DRAWINGML_DIAGRAMDATA_XML = (
        "application/vnd.openxmlformats-officedocument.drawingml.diagramData+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_DRAWINGML_DIAGRAMLAYOUT_XML = (
        "application/vnd.openxmlformats-officedocument.drawingml.diagramLayout+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_DRAWINGML_DIAGRAMSTYLE_XML = (
        "application/vnd.openxmlformats-officedocument.drawingml.diagramStyle+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_EXTENDED_PROPERTIES_XML = (
        "application/vnd.openxmlformats-officedocument.extended-properties+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_PRESENTATIONML_COMMENTAUTHORS_XML = (
        "application/vnd.openxmlformats-officedocument.presentationml.commentAuthors+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_PRESENTATIONML_COMMENTS_XML = (
        "application/vnd.openxmlformats-officedocument.presentationml.comments+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_PRESENTATIONML_HANDOUTMASTER_XML = (
        "application/vnd.openxmlformats-officedocument.presentationml.handoutMaster+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_PRESENTATIONML_NOTESMASTER_XML = (
        "application/vnd.openxmlformats-officedocument.presentationml.notesMaster+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_PRESENTATIONML_NOTESSLIDE_XML = (
        "application/vnd.openxmlformats-officedocument.presentationml.notesSlide+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_PRESENTATIONML_PRESENTATION = (
        "application/vnd.openxmlformats-officedocument.presentationml.presentation",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_PRESENTATIONML_PRESENTATION_MAIN_XML = (
        "application/vnd.openxmlformats-officedocument.presentationml.presentation.main+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_PRESENTATIONML_PRESPROPS_XML = (
        "application/vnd.openxmlformats-officedocument.presentationml.presProps+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_PRESENTATIONML_SLIDE = (
        "application/vnd.openxmlformats-officedocument.presentationml.slide",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_PRESENTATIONML_SLIDE_XML = (
        "application/vnd.openxmlformats-officedocument.presentationml.slide+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_PRESENTATIONML_SLIDELAYOUT_XML = (
        "application/vnd.openxmlformats-officedocument.presentationml.slideLayout+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_PRESENTATIONML_SLIDEMASTER_XML = (
        "application/vnd.openxmlformats-officedocument.presentationml.slideMaster+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_PRESENTATIONML_SLIDESHOW = (
        "application/vnd.openxmlformats-officedocument.presentationml.slideshow",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_PRESENTATIONML_SLIDESHOW_MAIN_XML = (
        "application/vnd.openxmlformats-officedocument.presentationml.slideshow.main+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_PRESENTATIONML_SLIDEUPDATEINFO_XML = (
        "application/vnd.openxmlformats-officedocument.presentationml.slideUpdateInfo+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_PRESENTATIONML_TABLESTYLES_XML = (
        "application/vnd.openxmlformats-officedocument.presentationml.tableStyles+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_PRESENTATIONML_TAGS_XML = (
        "application/vnd.openxmlformats-officedocument.presentationml.tags+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_PRESENTATIONML_TEMPLATE = (
        "application/vnd.openxmlformats-officedocument.presentationml.template",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_PRESENTATIONML_TEMPLATE_MAIN_XML = (
        "application/vnd.openxmlformats-officedocument.presentationml.template.main+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_PRESENTATIONML_VIEWPROPS_XML = (
        "application/vnd.openxmlformats-officedocument.presentationml.viewProps+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_SPREADSHEETML_CALCCHAIN_XML = (
        "application/vnd.openxmlformats-officedocument.spreadsheetml.calcChain+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_SPREADSHEETML_CHARTSHEET_XML = (
        "application/vnd.openxmlformats-officedocument.spreadsheetml.chartsheet+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_SPREADSHEETML_COMMENTS_XML = (
        "application/vnd.openxmlformats-officedocument.spreadsheetml.comments+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_SPREADSHEETML_CONNECTIONS_XML = (
        "application/vnd.openxmlformats-officedocument.spreadsheetml.connections+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_SPREADSHEETML_DIALOGSHEET_XML = (
        "application/vnd.openxmlformats-officedocument.spreadsheetml.dialogsheet+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_SPREADSHEETML_EXTERNALLINK_XML = (
        "application/vnd.openxmlformats-officedocument.spreadsheetml.externalLink+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_SPREADSHEETML_PIVOTCACHEDEFINITION_XML = (
        "application/vnd.openxmlformats-officedocument.spreadsheetml.pivotCacheDefinition+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_SPREADSHEETML_PIVOTCACHERECORDS_XML = (
        "application/vnd.openxmlformats-officedocument.spreadsheetml.pivotCacheRecords+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_SPREADSHEETML_PIVOTTABLE_XML = (
        "application/vnd.openxmlformats-officedocument.spreadsheetml.pivotTable+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_SPREADSHEETML_QUERYTABLE_XML = (
        "application/vnd.openxmlformats-officedocument.spreadsheetml.queryTable+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_SPREADSHEETML_REVISIONHEADERS_XML = (
        "application/vnd.openxmlformats-officedocument.spreadsheetml.revisionHeaders+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_SPREADSHEETML_REVISIONLOG_XML = (
        "application/vnd.openxmlformats-officedocument.spreadsheetml.revisionLog+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_SPREADSHEETML_SHAREDSTRINGS_XML = (
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sharedStrings+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_SPREADSHEETML_SHEET = (
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_SPREADSHEETML_SHEET_MAIN_XML = (
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet.main+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_SPREADSHEETML_SHEETMETADATA_XML = (
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheetMetadata+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_SPREADSHEETML_STYLES_XML = (
        "application/vnd.openxmlformats-officedocument.spreadsheetml.styles+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_SPREADSHEETML_TABLE_XML = (
        "application/vnd.openxmlformats-officedocument.spreadsheetml.table+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_SPREADSHEETML_TABLESINGLECELLS_XML = (
        "application/vnd.openxmlformats-officedocument.spreadsheetml.tableSingleCells+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_SPREADSHEETML_TEMPLATE = (
        "application/vnd.openxmlformats-officedocument.spreadsheetml.template",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_SPREADSHEETML_TEMPLATE_MAIN_XML = (
        "application/vnd.openxmlformats-officedocument.spreadsheetml.template.main+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_SPREADSHEETML_USERNAMES_XML = (
        "application/vnd.openxmlformats-officedocument.spreadsheetml.userNames+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_SPREADSHEETML_VOLATILEDEPENDENCIES_XML = (
        "application/vnd.openxmlformats-officedocument.spreadsheetml.volatileDependencies+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_SPREADSHEETML_WORKSHEET_XML = (
        "application/vnd.openxmlformats-officedocument.spreadsheetml.worksheet+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_THEME_XML = (
        "application/vnd.openxmlformats-officedocument.theme+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_THEMEOVERRIDE_XML = (
        "application/vnd.openxmlformats-officedocument.themeOverride+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_VMLDRAWING = (
        "application/vnd.openxmlformats-officedocument.vmlDrawing",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_WORDPROCESSINGML_COMMENTS_XML = (
        "application/vnd.openxmlformats-officedocument.wordprocessingml.comments+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_WORDPROCESSINGML_DOCUMENT = (
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_WORDPROCESSINGML_DOCUMENT_GLOSSARY_XML = (
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document.glossary+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_WORDPROCESSINGML_DOCUMENT_MAIN_XML = (
        "application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_WORDPROCESSINGML_ENDNOTES_XML = (
        "application/vnd.openxmlformats-officedocument.wordprocessingml.endnotes+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_WORDPROCESSINGML_FONTTABLE_XML = (
        "application/vnd.openxmlformats-officedocument.wordprocessingml.fontTable+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_WORDPROCESSINGML_FOOTER_XML = (
        "application/vnd.openxmlformats-officedocument.wordprocessingml.footer+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_WORDPROCESSINGML_FOOTNOTES_XML = (
        "application/vnd.openxmlformats-officedocument.wordprocessingml.footnotes+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_WORDPROCESSINGML_NUMBERING_XML = (
        "application/vnd.openxmlformats-officedocument.wordprocessingml.numbering+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_WORDPROCESSINGML_SETTINGS_XML = (
        "application/vnd.openxmlformats-officedocument.wordprocessingml.settings+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_WORDPROCESSINGML_STYLES_XML = (
        "application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_WORDPROCESSINGML_TEMPLATE = (
        "application/vnd.openxmlformats-officedocument.wordprocessingml.template",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_WORDPROCESSINGML_TEMPLATE_MAIN_XML = (
        "application/vnd.openxmlformats-officedocument.wordprocessingml.template.main+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_OFFICEDOCUMENT_WORDPROCESSINGML_WEBSETTINGS_XML = (
        "application/vnd.openxmlformats-officedocument.wordprocessingml.webSettings+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_PACKAGE_CORE_PROPERTIES_XML = (
        "application/vnd.openxmlformats-package.core-properties+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_PACKAGE_DIGITAL_SIGNATURE_XMLSIGNATURE_XML = (
        "application/vnd.openxmlformats-package.digital-signature-xmlsignature+xml",
    )
    FILEFORMAT_APPLICATION_VND_OPENXMLFORMATS_PACKAGE_RELATIONSHIPS_XML = (
        "application/vnd.openxmlformats-package.relationships+xml",
    )
    FILEFORMAT_APPLICATION_VND_ORACLE_RESOURCE_JSON = (
        "application/vnd.oracle.resource+json",
    )
    FILEFORMAT_APPLICATION_VND_ORANGE_INDATA = ("application/vnd.orange.indata",)
    FILEFORMAT_APPLICATION_VND_OSA_NETDEPLOY = ("application/vnd.osa.netdeploy",)
    FILEFORMAT_APPLICATION_VND_OSGEO_MAPGUIDE_PACKAGE = (
        "application/vnd.osgeo.mapguide.package",
    )
    FILEFORMAT_APPLICATION_VND_OSGI_BUNDLE = ("application/vnd.osgi.bundle",)
    FILEFORMAT_APPLICATION_VND_OSGI_DP = ("application/vnd.osgi.dp",)
    FILEFORMAT_APPLICATION_VND_OSGI_SUBSYSTEM = ("application/vnd.osgi.subsystem",)
    FILEFORMAT_APPLICATION_VND_OTPS_CT_KIP_XML = ("application/vnd.otps.ct-kip+xml",)
    FILEFORMAT_APPLICATION_VND_OXLI_COUNTGRAPH = ("application/vnd.oxli.countgraph",)
    FILEFORMAT_APPLICATION_VND_PAGERDUTY_JSON = ("application/vnd.pagerduty+json",)
    FILEFORMAT_APPLICATION_VND_PALM = ("application/vnd.palm",)
    FILEFORMAT_APPLICATION_VND_PANOPLY = ("application/vnd.panoply",)
    FILEFORMAT_APPLICATION_VND_PAOS_XML = ("application/vnd.paos.xml",)
    FILEFORMAT_APPLICATION_VND_PAWAAFILE = ("application/vnd.pawaafile",)
    FILEFORMAT_APPLICATION_VND_PCOS = ("application/vnd.pcos",)
    FILEFORMAT_APPLICATION_VND_PG_FORMAT = ("application/vnd.pg.format",)
    FILEFORMAT_APPLICATION_VND_PG_OSASLI = ("application/vnd.pg.osasli",)
    FILEFORMAT_APPLICATION_VND_PIACCESS_APPLICATION_LICENCE = (
        "application/vnd.piaccess.application-licence",
    )
    FILEFORMAT_APPLICATION_VND_PICSEL = ("application/vnd.picsel",)
    FILEFORMAT_APPLICATION_VND_PMI_WIDGET = ("application/vnd.pmi.widget",)
    FILEFORMAT_APPLICATION_VND_POC_GROUP_ADVERTISEMENT_XML = (
        "application/vnd.poc.group-advertisement+xml",
    )
    FILEFORMAT_APPLICATION_VND_POCKETLEARN = ("application/vnd.pocketlearn",)
    FILEFORMAT_APPLICATION_VND_POWERBUILDER6 = ("application/vnd.powerbuilder6",)
    FILEFORMAT_APPLICATION_VND_POWERBUILDER6_S = ("application/vnd.powerbuilder6-s",)
    FILEFORMAT_APPLICATION_VND_POWERBUILDER7 = ("application/vnd.powerbuilder7",)
    FILEFORMAT_APPLICATION_VND_POWERBUILDER75 = ("application/vnd.powerbuilder75",)
    FILEFORMAT_APPLICATION_VND_POWERBUILDER75_S = ("application/vnd.powerbuilder75-s",)
    FILEFORMAT_APPLICATION_VND_POWERBUILDER7_S = ("application/vnd.powerbuilder7-s",)
    FILEFORMAT_APPLICATION_VND_PREMINET = ("application/vnd.preminet",)
    FILEFORMAT_APPLICATION_VND_PREVIEWSYSTEMS_BOX = (
        "application/vnd.previewsystems.box",
    )
    FILEFORMAT_APPLICATION_VND_PROTEUS_MAGAZINE = ("application/vnd.proteus.magazine",)
    FILEFORMAT_APPLICATION_VND_PUBLISHARE_DELTA_TREE = (
        "application/vnd.publishare-delta-tree",
    )
    FILEFORMAT_APPLICATION_VND_PVI_PTID1 = ("application/vnd.pvi.ptid1",)
    FILEFORMAT_APPLICATION_VND_PWG_MULTIPLEXED = ("application/vnd.pwg-multiplexed",)
    FILEFORMAT_APPLICATION_VND_PWG_XHTML_PRINT_XML = (
        "application/vnd.pwg-xhtml-print+xml",
    )
    FILEFORMAT_APPLICATION_VND_QUALCOMM_BREW_APP_RES = (
        "application/vnd.qualcomm.brew-app-res",
    )
    FILEFORMAT_APPLICATION_VND_QUARANTAINENET = ("application/vnd.quarantainenet",)
    FILEFORMAT_APPLICATION_VND_QUARK_QUARKXPRESS = (
        "application/vnd.Quark.QuarkXPress",
    )
    FILEFORMAT_APPLICATION_VND_QUOBJECT_QUOXDOCUMENT = (
        "application/vnd.quobject-quoxdocument",
    )
    FILEFORMAT_APPLICATION_VND_RADISYS_MOML_XML = ("application/vnd.radisys.moml+xml",)
    FILEFORMAT_APPLICATION_VND_RADISYS_MSML_AUDITCONF_XML = (
        "application/vnd.radisys.msml-audit-conf+xml",
    )
    FILEFORMAT_APPLICATION_VND_RADISYS_MSML_AUDITCONN_XML = (
        "application/vnd.radisys.msml-audit-conn+xml",
    )
    FILEFORMAT_APPLICATION_VND_RADISYS_MSML_AUDIT_DIALOG_XML = (
        "application/vnd.radisys.msml-audit-dialog+xml",
    )
    FILEFORMAT_APPLICATION_VND_RADISYS_MSML_AUDIT_STREAM_XML = (
        "application/vnd.radisys.msml-audit-stream+xml",
    )
    FILEFORMAT_APPLICATION_VND_RADISYS_MSML_AUDIT_XML = (
        "application/vnd.radisys.msml-audit+xml",
    )
    FILEFORMAT_APPLICATION_VND_RADISYS_MSMLCONF_XML = (
        "application/vnd.radisys.msml-conf+xml",
    )
    FILEFORMAT_APPLICATION_VND_RADISYS_MSML_DIALOG_BASE_XML = (
        "application/vnd.radisys.msml-dialog-base+xml",
    )
    FILEFORMAT_APPLICATION_VND_RADISYS_MSML_DIALOG_FAX_DETECT_XML = (
        "application/vnd.radisys.msml-dialog-fax-detect+xml",
    )
    FILEFORMAT_APPLICATION_VND_RADISYS_MSML_DIALOG_FAX_SENDRECV_XML = (
        "application/vnd.radisys.msml-dialog-fax-sendrecv+xml",
    )
    FILEFORMAT_APPLICATION_VND_RADISYS_MSML_DIALOG_GROUP_XML = (
        "application/vnd.radisys.msml-dialog-group+xml",
    )
    FILEFORMAT_APPLICATION_VND_RADISYS_MSML_DIALOG_SPEECH_XML = (
        "application/vnd.radisys.msml-dialog-speech+xml",
    )
    FILEFORMAT_APPLICATION_VND_RADISYS_MSML_DIALOG_TRANSFORM_XML = (
        "application/vnd.radisys.msml-dialog-transform+xml",
    )
    FILEFORMAT_APPLICATION_VND_RADISYS_MSML_DIALOG_XML = (
        "application/vnd.radisys.msml-dialog+xml",
    )
    FILEFORMAT_APPLICATION_VND_RADISYS_MSML_XML = ("application/vnd.radisys.msml+xml",)
    FILEFORMAT_APPLICATION_VND_RAINSTOR_DATA = ("application/vnd.rainstor.data",)
    FILEFORMAT_APPLICATION_VND_RAPID = ("application/vnd.rapid",)
    FILEFORMAT_APPLICATION_VND_RAR = ("application/vnd.rar",)
    FILEFORMAT_APPLICATION_VND_REALVNC_BED = ("application/vnd.realvnc.bed",)
    FILEFORMAT_APPLICATION_VND_RECORDARE_MUSICXML = (
        "application/vnd.recordare.musicxml",
    )
    FILEFORMAT_APPLICATION_VND_RECORDARE_MUSICXML_XML = (
        "application/vnd.recordare.musicxml+xml",
    )
    FILEFORMAT_APPLICATION_VND_RENLEARN_RLPRINT = ("application/vnd.RenLearn.rlprint",)
    FILEFORMAT_APPLICATION_VND_RIG_CRYPTONOTE = ("application/vnd.rig.cryptonote",)
    FILEFORMAT_APPLICATION_VND_ROUTE66_LINK66_XML = (
        "application/vnd.route66.link66+xml",
    )
    FILEFORMAT_APPLICATION_VND_RS_274X = ("application/vnd.rs-274x",)
    FILEFORMAT_APPLICATION_VND_RUCKUS_DOWNLOAD = ("application/vnd.ruckus.download",)
    FILEFORMAT_APPLICATION_VND_S3SMS = ("application/vnd.s3sms",)
    FILEFORMAT_APPLICATION_VND_SAILINGTRACKER_TRACK = (
        "application/vnd.sailingtracker.track",
    )
    FILEFORMAT_APPLICATION_VND_SBM_CID = ("application/vnd.sbm.cid",)
    FILEFORMAT_APPLICATION_VND_SBM_MID2 = ("application/vnd.sbm.mid2",)
    FILEFORMAT_APPLICATION_VND_SCRIBUS = ("application/vnd.scribus",)
    FILEFORMAT_APPLICATION_VND_SEALED_3DF = ("application/vnd.sealed.3df",)
    FILEFORMAT_APPLICATION_VND_SEALED_CSF = ("application/vnd.sealed.csf",)
    FILEFORMAT_APPLICATION_VND_SEALED_DOC = ("application/vnd.sealed.doc",)
    FILEFORMAT_APPLICATION_VND_SEALED_EML = ("application/vnd.sealed.eml",)
    FILEFORMAT_APPLICATION_VND_SEALED_MHT = ("application/vnd.sealed.mht",)
    FILEFORMAT_APPLICATION_VND_SEALED_NET = ("application/vnd.sealed.net",)
    FILEFORMAT_APPLICATION_VND_SEALED_PPT = ("application/vnd.sealed.ppt",)
    FILEFORMAT_APPLICATION_VND_SEALED_TIFF = ("application/vnd.sealed.tiff",)
    FILEFORMAT_APPLICATION_VND_SEALED_XLS = ("application/vnd.sealed.xls",)
    FILEFORMAT_APPLICATION_VND_SEALEDMEDIA_SOFTSEAL_HTML = (
        "application/vnd.sealedmedia.softseal.html",
    )
    FILEFORMAT_APPLICATION_VND_SEALEDMEDIA_SOFTSEAL_PDF = (
        "application/vnd.sealedmedia.softseal.pdf",
    )
    FILEFORMAT_APPLICATION_VND_SEEMAIL = ("application/vnd.seemail",)
    FILEFORMAT_APPLICATION_VND_SEMA = ("application/vnd.sema",)
    FILEFORMAT_APPLICATION_VND_SEMD = ("application/vnd.semd",)
    FILEFORMAT_APPLICATION_VND_SEMF = ("application/vnd.semf",)
    FILEFORMAT_APPLICATION_VND_SHANA_INFORMED_FORMDATA = (
        "application/vnd.shana.informed.formdata",
    )
    FILEFORMAT_APPLICATION_VND_SHANA_INFORMED_FORMTEMPLATE = (
        "application/vnd.shana.informed.formtemplate",
    )
    FILEFORMAT_APPLICATION_VND_SHANA_INFORMED_INTERCHANGE = (
        "application/vnd.shana.informed.interchange",
    )
    FILEFORMAT_APPLICATION_VND_SHANA_INFORMED_PACKAGE = (
        "application/vnd.shana.informed.package",
    )
    FILEFORMAT_APPLICATION_VND_SIGROK_SESSION = ("application/vnd.sigrok.session",)
    FILEFORMAT_APPLICATION_VND_SIMTECH_MINDMAPPER = (
        "application/vnd.SimTech-MindMapper",
    )
    FILEFORMAT_APPLICATION_VND_SIREN_JSON = ("application/vnd.siren+json",)
    FILEFORMAT_APPLICATION_VND_SMAF = ("application/vnd.smaf",)
    FILEFORMAT_APPLICATION_VND_SMART_NOTEBOOK = ("application/vnd.smart.notebook",)
    FILEFORMAT_APPLICATION_VND_SMART_TEACHER = ("application/vnd.smart.teacher",)
    FILEFORMAT_APPLICATION_VND_SOFTWARE602_FILLER_FORM_XML = (
        "application/vnd.software602.filler.form+xml",
    )
    FILEFORMAT_APPLICATION_VND_SOFTWARE602_FILLER_FORM_XML_ZIP = (
        "application/vnd.software602.filler.form-xml-zip",
    )
    FILEFORMAT_APPLICATION_VND_SOLENT_SDKM_XML = ("application/vnd.solent.sdkm+xml",)
    FILEFORMAT_APPLICATION_VND_SPOTFIRE_DXP = ("application/vnd.spotfire.dxp",)
    FILEFORMAT_APPLICATION_VND_SPOTFIRE_SFS = ("application/vnd.spotfire.sfs",)
    FILEFORMAT_APPLICATION_VND_SSSCOD = ("application/vnd.sss-cod",)
    FILEFORMAT_APPLICATION_VND_SSS_DTF = ("application/vnd.sss-dtf",)
    FILEFORMAT_APPLICATION_VND_SSS_NTF = ("application/vnd.sss-ntf",)
    FILEFORMAT_APPLICATION_VND_STEPMANIA_PACKAGE = (
        "application/vnd.stepmania.package",
    )
    FILEFORMAT_APPLICATION_VND_STEPMANIA_STEPCHART = (
        "application/vnd.stepmania.stepchart",
    )
    FILEFORMAT_APPLICATION_VND_STREET_STREAM = ("application/vnd.street-stream",)
    FILEFORMAT_APPLICATION_VND_SUN_WADL_XML = ("application/vnd.sun.wadl+xml",)
    FILEFORMAT_APPLICATION_VND_SUSCALENDAR = ("application/vnd.sus-calendar",)
    FILEFORMAT_APPLICATION_VND_SVD = ("application/vnd.svd",)
    FILEFORMAT_APPLICATION_VND_SWIFTVIEW_ICS = ("application/vnd.swiftview-ics",)
    FILEFORMAT_APPLICATION_VND_SYNCML_DM_NOTIFICATION = (
        "application/vnd.syncml.dm.notification",
    )
    FILEFORMAT_APPLICATION_VND_SYNCML_DMDDF_XML = ("application/vnd.syncml.dmddf+xml",)
    FILEFORMAT_APPLICATION_VND_SYNCML_DMTNDS_WBXML = (
        "application/vnd.syncml.dmtnds+wbxml",
    )
    FILEFORMAT_APPLICATION_VND_SYNCML_DMTNDS_XML = (
        "application/vnd.syncml.dmtnds+xml",
    )
    FILEFORMAT_APPLICATION_VND_SYNCML_DMDDF_WBXML = (
        "application/vnd.syncml.dmddf+wbxml",
    )
    FILEFORMAT_APPLICATION_VND_SYNCML_DM_WBXML = ("application/vnd.syncml.dm+wbxml",)
    FILEFORMAT_APPLICATION_VND_SYNCML_DM_XML = ("application/vnd.syncml.dm+xml",)
    FILEFORMAT_APPLICATION_VND_SYNCML_DS_NOTIFICATION = (
        "application/vnd.syncml.ds.notification",
    )
    FILEFORMAT_APPLICATION_VND_SYNCML_XML = ("application/vnd.syncml+xml",)
    FILEFORMAT_APPLICATION_VND_TABLESCHEMA_JSON = ("application/vnd.tableschema+json",)
    FILEFORMAT_APPLICATION_VND_TAO_INTENT_MODULE_ARCHIVE = (
        "application/vnd.tao.intent-module-archive",
    )
    FILEFORMAT_APPLICATION_VND_TCPDUMP_PCAP = ("application/vnd.tcpdump.pcap",)
    FILEFORMAT_APPLICATION_VND_TML = ("application/vnd.tml",)
    FILEFORMAT_APPLICATION_VND_TMD_MEDIAFLEX_API_XML = (
        "application/vnd.tmd.mediaflex.api+xml",
    )
    FILEFORMAT_APPLICATION_VND_TMOBILE_LIVETV = ("application/vnd.tmobile-livetv",)
    FILEFORMAT_APPLICATION_VND_TRI_ONESOURCE = ("application/vnd.tri.onesource",)
    FILEFORMAT_APPLICATION_VND_TRID_TPT = ("application/vnd.trid.tpt",)
    FILEFORMAT_APPLICATION_VND_TRISCAPE_MXS = ("application/vnd.triscape.mxs",)
    FILEFORMAT_APPLICATION_VND_TRUEAPP = ("application/vnd.trueapp",)
    FILEFORMAT_APPLICATION_VND_TRUEDOC = ("application/vnd.truedoc",)
    FILEFORMAT_APPLICATION_VND_UBISOFT_WEBPLAYER = (
        "application/vnd.ubisoft.webplayer",
    )
    FILEFORMAT_APPLICATION_VND_UFDL = ("application/vnd.ufdl",)
    FILEFORMAT_APPLICATION_VND_UIQ_THEME = ("application/vnd.uiq.theme",)
    FILEFORMAT_APPLICATION_VND_UMAJIN = ("application/vnd.umajin",)
    FILEFORMAT_APPLICATION_VND_UNITY = ("application/vnd.unity",)
    FILEFORMAT_APPLICATION_VND_UOML_XML = ("application/vnd.uoml+xml",)
    FILEFORMAT_APPLICATION_VND_UPLANET_ALERT = ("application/vnd.uplanet.alert",)
    FILEFORMAT_APPLICATION_VND_UPLANET_ALERT_WBXML = (
        "application/vnd.uplanet.alert-wbxml",
    )
    FILEFORMAT_APPLICATION_VND_UPLANET_BEARERCHOICE = (
        "application/vnd.uplanet.bearer-choice",
    )
    FILEFORMAT_APPLICATION_VND_UPLANET_BEARERCHOICE_WBXML = (
        "application/vnd.uplanet.bearer-choice-wbxml",
    )
    FILEFORMAT_APPLICATION_VND_UPLANET_CACHEOP = ("application/vnd.uplanet.cacheop",)
    FILEFORMAT_APPLICATION_VND_UPLANET_CACHEOP_WBXML = (
        "application/vnd.uplanet.cacheop-wbxml",
    )
    FILEFORMAT_APPLICATION_VND_UPLANET_CHANNEL = ("application/vnd.uplanet.channel",)
    FILEFORMAT_APPLICATION_VND_UPLANET_CHANNEL_WBXML = (
        "application/vnd.uplanet.channel-wbxml",
    )
    FILEFORMAT_APPLICATION_VND_UPLANET_LIST = ("application/vnd.uplanet.list",)
    FILEFORMAT_APPLICATION_VND_UPLANET_LISTCMD = ("application/vnd.uplanet.listcmd",)
    FILEFORMAT_APPLICATION_VND_UPLANET_LISTCMD_WBXML = (
        "application/vnd.uplanet.listcmd-wbxml",
    )
    FILEFORMAT_APPLICATION_VND_UPLANET_LIST_WBXML = (
        "application/vnd.uplanet.list-wbxml",
    )
    FILEFORMAT_APPLICATION_VND_URI_MAP = ("application/vnd.uri-map",)
    FILEFORMAT_APPLICATION_VND_UPLANET_SIGNAL = ("application/vnd.uplanet.signal",)
    FILEFORMAT_APPLICATION_VND_VALVE_SOURCE_MATERIAL = (
        "application/vnd.valve.source.material",
    )
    FILEFORMAT_APPLICATION_VND_VCX = ("application/vnd.vcx",)
    FILEFORMAT_APPLICATION_VND_VD_STUDY = ("application/vnd.vd-study",)
    FILEFORMAT_APPLICATION_VND_VECTORWORKS = ("application/vnd.vectorworks",)
    FILEFORMAT_APPLICATION_VND_VEL_JSON = ("application/vnd.vel+json",)
    FILEFORMAT_APPLICATION_VND_VERIMATRIX_VCAS = ("application/vnd.verimatrix.vcas",)
    FILEFORMAT_APPLICATION_VND_VIDSOFT_VIDCONFERENCE = (
        "application/vnd.vidsoft.vidconference",
    )
    FILEFORMAT_APPLICATION_VND_VISIO = ("application/vnd.visio",)
    FILEFORMAT_APPLICATION_VND_VISIONARY = ("application/vnd.visionary",)
    FILEFORMAT_APPLICATION_VND_VIVIDENCE_SCRIPTFILE = (
        "application/vnd.vividence.scriptfile",
    )
    FILEFORMAT_APPLICATION_VND_VSF = ("application/vnd.vsf",)
    FILEFORMAT_APPLICATION_VND_WAP_SIC = ("application/vnd.wap.sic",)
    FILEFORMAT_APPLICATION_VND_WAP_SLC = ("application/vnd.wap.slc",)
    FILEFORMAT_APPLICATION_VND_WAP_WBXML = ("application/vnd.wap.wbxml",)
    FILEFORMAT_APPLICATION_VND_WAP_WMLC = ("application/vnd.wap.wmlc",)
    FILEFORMAT_APPLICATION_VND_WAP_WMLSCRIPTC = ("application/vnd.wap.wmlscriptc",)
    FILEFORMAT_APPLICATION_VND_WEBTURBO = ("application/vnd.webturbo",)
    FILEFORMAT_APPLICATION_VND_WFA_P2P = ("application/vnd.wfa.p2p",)
    FILEFORMAT_APPLICATION_VND_WFA_WSC = ("application/vnd.wfa.wsc",)
    FILEFORMAT_APPLICATION_VND_WINDOWS_DEVICEPAIRING = (
        "application/vnd.windows.devicepairing",
    )
    FILEFORMAT_APPLICATION_VND_WMC = ("application/vnd.wmc",)
    FILEFORMAT_APPLICATION_VND_WMF_BOOTSTRAP = ("application/vnd.wmf.bootstrap",)
    FILEFORMAT_APPLICATION_VND_WOLFRAM_MATHEMATICA = (
        "application/vnd.wolfram.mathematica",
    )
    FILEFORMAT_APPLICATION_VND_WOLFRAM_MATHEMATICA_PACKAGE = (
        "application/vnd.wolfram.mathematica.package",
    )
    FILEFORMAT_APPLICATION_VND_WOLFRAM_PLAYER = ("application/vnd.wolfram.player",)
    FILEFORMAT_APPLICATION_VND_WORDPERFECT = ("application/vnd.wordperfect",)
    FILEFORMAT_APPLICATION_VND_WQD = ("application/vnd.wqd",)
    FILEFORMAT_APPLICATION_VND_WRQ_HP3000_LABELLED = (
        "application/vnd.wrq-hp3000-labelled",
    )
    FILEFORMAT_APPLICATION_VND_WT_STF = ("application/vnd.wt.stf",)
    FILEFORMAT_APPLICATION_VND_WV_CSP_XML = ("application/vnd.wv.csp+xml",)
    FILEFORMAT_APPLICATION_VND_WV_CSP_WBXML = ("application/vnd.wv.csp+wbxml",)
    FILEFORMAT_APPLICATION_VND_WV_SSP_XML = ("application/vnd.wv.ssp+xml",)
    FILEFORMAT_APPLICATION_VND_XACML_JSON = ("application/vnd.xacml+json",)
    FILEFORMAT_APPLICATION_VND_XARA = ("application/vnd.xara",)
    FILEFORMAT_APPLICATION_VND_XFDL = ("application/vnd.xfdl",)
    FILEFORMAT_APPLICATION_VND_XFDL_WEBFORM = ("application/vnd.xfdl.webform",)
    FILEFORMAT_APPLICATION_VND_XMI_XML = ("application/vnd.xmi+xml",)
    FILEFORMAT_APPLICATION_VND_XMPIE_CPKG = ("application/vnd.xmpie.cpkg",)
    FILEFORMAT_APPLICATION_VND_XMPIE_DPKG = ("application/vnd.xmpie.dpkg",)
    FILEFORMAT_APPLICATION_VND_XMPIE_PLAN = ("application/vnd.xmpie.plan",)
    FILEFORMAT_APPLICATION_VND_XMPIE_PPKG = ("application/vnd.xmpie.ppkg",)
    FILEFORMAT_APPLICATION_VND_XMPIE_XLIM = ("application/vnd.xmpie.xlim",)
    FILEFORMAT_APPLICATION_VND_YAMAHA_HV_DIC = ("application/vnd.yamaha.hv-dic",)
    FILEFORMAT_APPLICATION_VND_YAMAHA_HV_SCRIPT = ("application/vnd.yamaha.hv-script",)
    FILEFORMAT_APPLICATION_VND_YAMAHA_HV_VOICE = ("application/vnd.yamaha.hv-voice",)
    FILEFORMAT_APPLICATION_VND_YAMAHA_OPENSCOREFORMAT_OSFPVG_XML = (
        "application/vnd.yamaha.openscoreformat.osfpvg+xml",
    )
    FILEFORMAT_APPLICATION_VND_YAMAHA_OPENSCOREFORMAT = (
        "application/vnd.yamaha.openscoreformat",
    )
    FILEFORMAT_APPLICATION_VND_YAMAHA_REMOTE_SETUP = (
        "application/vnd.yamaha.remote-setup",
    )
    FILEFORMAT_APPLICATION_VND_YAMAHA_SMAF_AUDIO = (
        "application/vnd.yamaha.smaf-audio",
    )
    FILEFORMAT_APPLICATION_VND_YAMAHA_SMAF_PHRASE = (
        "application/vnd.yamaha.smaf-phrase",
    )
    FILEFORMAT_APPLICATION_VND_YAMAHA_THROUGH_NGN = (
        "application/vnd.yamaha.through-ngn",
    )
    FILEFORMAT_APPLICATION_VND_YAMAHA_TUNNEL_UDPENCAP = (
        "application/vnd.yamaha.tunnel-udpencap",
    )
    FILEFORMAT_APPLICATION_VND_YAOWEME = ("application/vnd.yaoweme",)
    FILEFORMAT_APPLICATION_VND_YELLOWRIVERCUSTOM_MENU = (
        "application/vnd.yellowriver-custom-menu",
    )
    FILEFORMAT_APPLICATION_VND_ZUL = ("application/vnd.zul",)
    FILEFORMAT_APPLICATION_VND_ZZAZZ_DECK_XML = ("application/vnd.zzazz.deck+xml",)
    FILEFORMAT_APPLICATION_VOICEXML_XML = ("application/voicexml+xml",)
    FILEFORMAT_APPLICATION_VQ_RTCPXR = ("application/vq-rtcpxr",)
    FILEFORMAT_APPLICATION_WATCHERINFO_XML = ("application/watcherinfo+xml",)
    FILEFORMAT_APPLICATION_WHOISPP_QUERY = ("application/whoispp-query",)
    FILEFORMAT_APPLICATION_WHOISPP_RESPONSE = ("application/whoispp-response",)
    FILEFORMAT_APPLICATION_WIDGET = ("application/widget",)
    FILEFORMAT_APPLICATION_WITA = ("application/wita",)
    FILEFORMAT_APPLICATION_WORDPERFECT5_1 = ("application/wordperfect5.1",)
    FILEFORMAT_APPLICATION_WSDL_XML = ("application/wsdl+xml",)
    FILEFORMAT_APPLICATION_WSPOLICY_XML = ("application/wspolicy+xml",)
    FILEFORMAT_APPLICATION_X_WWW_FORM_URLENCODED = (
        "application/x-www-form-urlencoded",
    )
    FILEFORMAT_APPLICATION_X400_BP = ("application/x400-bp",)
    FILEFORMAT_APPLICATION_XACML_XML = ("application/xacml+xml",)
    FILEFORMAT_APPLICATION_XCAP_ATT_XML = ("application/xcap-att+xml",)
    FILEFORMAT_APPLICATION_XCAPCAPS_XML = ("application/xcap-caps+xml",)
    FILEFORMAT_APPLICATION_XCAP_DIFF_XML = ("application/xcap-diff+xml",)
    FILEFORMAT_APPLICATION_XCAP_EL_XML = ("application/xcap-el+xml",)
    FILEFORMAT_APPLICATION_XCAP_ERROR_XML = ("application/xcap-error+xml",)
    FILEFORMAT_APPLICATION_XCAP_NS_XML = ("application/xcap-ns+xml",)
    FILEFORMAT_APPLICATION_XCONCONFERENCE_INFO_DIFF_XML = (
        "application/xcon-conference-info-diff+xml",
    )
    FILEFORMAT_APPLICATION_XCONCONFERENCE_INFO_XML = (
        "application/xcon-conference-info+xml",
    )
    FILEFORMAT_APPLICATION_XENC_XML = ("application/xenc+xml",)
    FILEFORMAT_APPLICATION_XHTML_VOICE_XML = ("application/xhtml-voice+xml",)
    FILEFORMAT_APPLICATION_XHTML_XML = ("application/xhtml+xml",)
    FILEFORMAT_APPLICATION_XML = ("application/xml",)
    FILEFORMAT_APPLICATION_XML_DTD = ("application/xml-dtd",)
    FILEFORMAT_APPLICATION_XML_EXTERNAL_PARSED_ENTITY = (
        "application/xml-external-parsed-entity",
    )
    FILEFORMAT_APPLICATION_XML_PATCH_XML = ("application/xml-patch+xml",)
    FILEFORMAT_APPLICATION_XMPP_XML = ("application/xmpp+xml",)
    FILEFORMAT_APPLICATION_XOP_XML = ("application/xop+xml",)
    FILEFORMAT_APPLICATION_XSLT_XML = ("application/xslt+xml",)
    FILEFORMAT_APPLICATION_XV_XML = ("application/xv+xml",)
    FILEFORMAT_APPLICATION_YANG = ("application/yang",)
    FILEFORMAT_APPLICATION_YANG_DATA_JSON = ("application/yang-data+json",)
    FILEFORMAT_APPLICATION_YANG_DATA_XML = ("application/yang-data+xml",)
    FILEFORMAT_APPLICATION_YANG_PATCH_JSON = ("application/yang-patch+json",)
    FILEFORMAT_APPLICATION_YANG_PATCH_XML = ("application/yang-patch+xml",)
    FILEFORMAT_APPLICATION_YIN_XML = ("application/yin+xml",)
    FILEFORMAT_APPLICATION_ZIP = ("application/zip",)
    FILEFORMAT_APPLICATION_ZLIB = ("application/zlib",)
    FILEFORMAT_AUDIO_1D_INTERLEAVED_PARITYFEC = ("audio/1d-interleaved-parityfec",)
    FILEFORMAT_AUDIO_32KADPCM = ("audio/32kadpcm",)
    FILEFORMAT_AUDIO_3GPP = ("audio/3gpp",)
    FILEFORMAT_AUDIO_3GPP2 = ("audio/3gpp2",)
    FILEFORMAT_AUDIO_AC3 = ("audio/ac3",)
    FILEFORMAT_AUDIO_AMR = ("audio/AMR",)
    FILEFORMAT_AUDIO_AMR_WB = ("audio/AMR-WB",)
    FILEFORMAT_AUDIO_AMR_WB_ = ("audio/amr-wb+",)
    FILEFORMAT_AUDIO_APTX = ("audio/aptx",)
    FILEFORMAT_AUDIO_ASC = ("audio/asc",)
    FILEFORMAT_AUDIO_ATRAC_ADVANCED_LOSSLESS = ("audio/ATRAC-ADVANCED-LOSSLESS",)
    FILEFORMAT_AUDIO_ATRAC_X = ("audio/ATRAC-X",)
    FILEFORMAT_AUDIO_ATRAC3 = ("audio/ATRAC3",)
    FILEFORMAT_AUDIO_BASIC = ("audio/basic",)
    FILEFORMAT_AUDIO_BV16 = ("audio/BV16",)
    FILEFORMAT_AUDIO_BV32 = ("audio/BV32",)
    FILEFORMAT_AUDIO_CLEARMODE = ("audio/clearmode",)
    FILEFORMAT_AUDIO_CN = ("audio/CN",)
    FILEFORMAT_AUDIO_DAT12 = ("audio/DAT12",)
    FILEFORMAT_AUDIO_DLS = ("audio/dls",)
    FILEFORMAT_AUDIO_DSR_ES201108 = ("audio/dsr-es201108",)
    FILEFORMAT_AUDIO_DSR_ES202050 = ("audio/dsr-es202050",)
    FILEFORMAT_AUDIO_DSR_ES202211 = ("audio/dsr-es202211",)
    FILEFORMAT_AUDIO_DSR_ES202212 = ("audio/dsr-es202212",)
    FILEFORMAT_AUDIO_DV = ("audio/DV",)
    FILEFORMAT_AUDIO_DVI4 = ("audio/DVI4",)
    FILEFORMAT_AUDIO_EAC3 = ("audio/eac3",)
    FILEFORMAT_AUDIO_ENCAPRTP = ("audio/encaprtp",)
    FILEFORMAT_AUDIO_EVRC = ("audio/EVRC",)
    FILEFORMAT_AUDIO_EVRC_QCP = ("audio/EVRC-QCP",)
    FILEFORMAT_AUDIO_EVRC0 = ("audio/EVRC0",)
    FILEFORMAT_AUDIO_EVRC1 = ("audio/EVRC1",)
    FILEFORMAT_AUDIO_EVRCB = ("audio/EVRCB",)
    FILEFORMAT_AUDIO_EVRCB0 = ("audio/EVRCB0",)
    FILEFORMAT_AUDIO_EVRCB1 = ("audio/EVRCB1",)
    FILEFORMAT_AUDIO_EVRCNW = ("audio/EVRCNW",)
    FILEFORMAT_AUDIO_EVRCNW0 = ("audio/EVRCNW0",)
    FILEFORMAT_AUDIO_EVRCNW1 = ("audio/EVRCNW1",)
    FILEFORMAT_AUDIO_EVRCWB = ("audio/EVRCWB",)
    FILEFORMAT_AUDIO_EVRCWB0 = ("audio/EVRCWB0",)
    FILEFORMAT_AUDIO_EVRCWB1 = ("audio/EVRCWB1",)
    FILEFORMAT_AUDIO_EVS = ("audio/EVS",)
    FILEFORMAT_AUDIO_EXAMPLE = ("audio/example",)
    FILEFORMAT_AUDIO_FWDRED = ("audio/fwdred",)
    FILEFORMAT_AUDIO_G711_0 = ("audio/G711-0",)
    FILEFORMAT_AUDIO_G719 = ("audio/G719",)
    FILEFORMAT_AUDIO_G7221 = ("audio/G7221",)
    FILEFORMAT_AUDIO_G722 = ("audio/G722",)
    FILEFORMAT_AUDIO_G723 = ("audio/G723",)
    FILEFORMAT_AUDIO_G726_16 = ("audio/G726-16",)
    FILEFORMAT_AUDIO_G726_24 = ("audio/G726-24",)
    FILEFORMAT_AUDIO_G726_32 = ("audio/G726-32",)
    FILEFORMAT_AUDIO_G726_40 = ("audio/G726-40",)
    FILEFORMAT_AUDIO_G728 = ("audio/G728",)
    FILEFORMAT_AUDIO_G729 = ("audio/G729",)
    FILEFORMAT_AUDIO_G7291 = ("audio/G7291",)
    FILEFORMAT_AUDIO_G729D = ("audio/G729D",)
    FILEFORMAT_AUDIO_G729E = ("audio/G729E",)
    FILEFORMAT_AUDIO_GSM = ("audio/GSM",)
    FILEFORMAT_AUDIO_GSM_EFR = ("audio/GSM-EFR",)
    FILEFORMAT_AUDIO_GSM_HR_08 = ("audio/GSM-HR-08",)
    FILEFORMAT_AUDIO_ILBC = ("audio/iLBC",)
    FILEFORMAT_AUDIO_IP_MR_V2_5 = ("audio/ip-mr_v2.5",)
    FILEFORMAT_AUDIO_L8 = ("audio/L8",)
    FILEFORMAT_AUDIO_L16 = ("audio/L16",)
    FILEFORMAT_AUDIO_L20 = ("audio/L20",)
    FILEFORMAT_AUDIO_L24 = ("audio/L24",)
    FILEFORMAT_AUDIO_LPC = ("audio/LPC",)
    FILEFORMAT_AUDIO_MELP = ("audio/MELP",)
    FILEFORMAT_AUDIO_MELP600 = ("audio/MELP600",)
    FILEFORMAT_AUDIO_MELP1200 = ("audio/MELP1200",)
    FILEFORMAT_AUDIO_MELP2400 = ("audio/MELP2400",)
    FILEFORMAT_AUDIO_MOBILE_XMF = ("audio/mobile-xmf",)
    FILEFORMAT_AUDIO_MPA = ("audio/MPA",)
    FILEFORMAT_AUDIO_MP4 = ("audio/mp4",)
    FILEFORMAT_AUDIO_MP4A_LATM = ("audio/MP4A-LATM",)
    FILEFORMAT_AUDIO_MPA_ROBUST = ("audio/mpa-robust",)
    FILEFORMAT_AUDIO_MPEG = ("audio/mpeg",)
    FILEFORMAT_AUDIO_MPEG4_GENERIC = ("audio/mpeg4-generic",)
    FILEFORMAT_AUDIO_OGG = ("audio/ogg",)
    FILEFORMAT_AUDIO_OPUS = ("audio/opus",)
    FILEFORMAT_AUDIO_PARITYFEC = ("audio/parityfec",)
    FILEFORMAT_AUDIO_PCMA = ("audio/PCMA",)
    FILEFORMAT_AUDIO_PCMA_WB = ("audio/PCMA-WB",)
    FILEFORMAT_AUDIO_PCMU = ("audio/PCMU",)
    FILEFORMAT_AUDIO_PCMU_WB = ("audio/PCMU-WB",)
    FILEFORMAT_AUDIO_PRS_SID = ("audio/prs.sid",)
    FILEFORMAT_AUDIO_QCELP = ("audio/QCELP",)
    FILEFORMAT_AUDIO_RAPTORFEC = ("audio/raptorfec",)
    FILEFORMAT_AUDIO_RED = ("audio/RED",)
    FILEFORMAT_AUDIO_RTP_ENC_AESCM128 = ("audio/rtp-enc-aescm128",)
    FILEFORMAT_AUDIO_RTPLOOPBACK = ("audio/rtploopback",)
    FILEFORMAT_AUDIO_RTP_MIDI = ("audio/rtp-midi",)
    FILEFORMAT_AUDIO_RTX = ("audio/rtx",)
    FILEFORMAT_AUDIO_SMV = ("audio/SMV",)
    FILEFORMAT_AUDIO_SMV0 = ("audio/SMV0",)
    FILEFORMAT_AUDIO_SMV_QCP = ("audio/SMV-QCP",)
    FILEFORMAT_AUDIO_SP_MIDI = ("audio/sp-midi",)
    FILEFORMAT_AUDIO_SPEEX = ("audio/speex",)
    FILEFORMAT_AUDIO_T140C = ("audio/t140c",)
    FILEFORMAT_AUDIO_T38 = ("audio/t38",)
    FILEFORMAT_AUDIO_TELEPHONE_EVENT = ("audio/telephone-event",)
    FILEFORMAT_AUDIO_TONE = ("audio/tone",)
    FILEFORMAT_AUDIO_UEMCLIP = ("audio/UEMCLIP",)
    FILEFORMAT_AUDIO_ULPFEC = ("audio/ulpfec",)
    FILEFORMAT_AUDIO_VDVI = ("audio/VDVI",)
    FILEFORMAT_AUDIO_VMR_WB = ("audio/VMR-WB",)
    FILEFORMAT_AUDIO_VND_3GPP_IUFP = ("audio/vnd.3gpp.iufp",)
    FILEFORMAT_AUDIO_VND_4SB = ("audio/vnd.4SB",)
    FILEFORMAT_AUDIO_VND_AUDIOKOZ = ("audio/vnd.audiokoz",)
    FILEFORMAT_AUDIO_VND_CELP = ("audio/vnd.CELP",)
    FILEFORMAT_AUDIO_VND_CISCO_NSE = ("audio/vnd.cisco.nse",)
    FILEFORMAT_AUDIO_VND_CMLES_RADIO_EVENTS = ("audio/vnd.cmles.radio-events",)
    FILEFORMAT_AUDIO_VND_CNS_ANP1 = ("audio/vnd.cns.anp1",)
    FILEFORMAT_AUDIO_VND_CNS_INF1 = ("audio/vnd.cns.inf1",)
    FILEFORMAT_AUDIO_VND_DECE_AUDIO = ("audio/vnd.dece.audio",)
    FILEFORMAT_AUDIO_VND_DIGITAL_WINDS = ("audio/vnd.digital-winds",)
    FILEFORMAT_AUDIO_VND_DLNA_ADTS = ("audio/vnd.dlna.adts",)
    FILEFORMAT_AUDIO_VND_DOLBY_HEAAC_1 = ("audio/vnd.dolby.heaac.1",)
    FILEFORMAT_AUDIO_VND_DOLBY_HEAAC_2 = ("audio/vnd.dolby.heaac.2",)
    FILEFORMAT_AUDIO_VND_DOLBY_MLP = ("audio/vnd.dolby.mlp",)
    FILEFORMAT_AUDIO_VND_DOLBY_MPS = ("audio/vnd.dolby.mps",)
    FILEFORMAT_AUDIO_VND_DOLBY_PL2 = ("audio/vnd.dolby.pl2",)
    FILEFORMAT_AUDIO_VND_DOLBY_PL2X = ("audio/vnd.dolby.pl2x",)
    FILEFORMAT_AUDIO_VND_DOLBY_PL2Z = ("audio/vnd.dolby.pl2z",)
    FILEFORMAT_AUDIO_VND_DOLBY_PULSE_1 = ("audio/vnd.dolby.pulse.1",)
    FILEFORMAT_AUDIO_VND_DRA = ("audio/vnd.dra",)
    FILEFORMAT_AUDIO_VND_DTS = ("audio/vnd.dts",)
    FILEFORMAT_AUDIO_VND_DTS_HD = ("audio/vnd.dts.hd",)
    FILEFORMAT_AUDIO_VND_DVB_FILE = ("audio/vnd.dvb.file",)
    FILEFORMAT_AUDIO_VND_EVERAD_PLJ = ("audio/vnd.everad.plj",)
    FILEFORMAT_AUDIO_VND_HNS_AUDIO = ("audio/vnd.hns.audio",)
    FILEFORMAT_AUDIO_VND_LUCENT_VOICE = ("audio/vnd.lucent.voice",)
    FILEFORMAT_AUDIO_VND_MS_PLAYREADY_MEDIA_PYA = ("audio/vnd.ms-playready.media.pya",)
    FILEFORMAT_AUDIO_VND_NOKIA_MOBILE_XMF = ("audio/vnd.nokia.mobile-xmf",)
    FILEFORMAT_AUDIO_VND_NORTEL_VBK = ("audio/vnd.nortel.vbk",)
    FILEFORMAT_AUDIO_VND_NUERA_ECELP4800 = ("audio/vnd.nuera.ecelp4800",)
    FILEFORMAT_AUDIO_VND_NUERA_ECELP7470 = ("audio/vnd.nuera.ecelp7470",)
    FILEFORMAT_AUDIO_VND_NUERA_ECELP9600 = ("audio/vnd.nuera.ecelp9600",)
    FILEFORMAT_AUDIO_VND_OCTEL_SBC = ("audio/vnd.octel.sbc",)
    FILEFORMAT_AUDIO_VND_QCELP = ("audio/vnd.qcelp",)
    FILEFORMAT_AUDIO_VND_RHETOREX_32KADPCM = ("audio/vnd.rhetorex.32kadpcm",)
    FILEFORMAT_AUDIO_VND_RIP = ("audio/vnd.rip",)
    FILEFORMAT_AUDIO_VND_SEALEDMEDIA_SOFTSEAL_MPEG = (
        "audio/vnd.sealedmedia.softseal.mpeg",
    )
    FILEFORMAT_AUDIO_VND_VMX_CVSD = ("audio/vnd.vmx.cvsd",)
    FILEFORMAT_AUDIO_VORBIS = ("audio/vorbis",)
    FILEFORMAT_AUDIO_VORBISCONFIG = ("audio/vorbis-config",)
    FILEFORMAT_FONT_COLLECTION = ("font/collection",)
    FILEFORMAT_FONT_OTF = ("font/otf",)
    FILEFORMAT_FONT_SFNT = ("font/sfnt",)
    FILEFORMAT_FONT_TTF = ("font/ttf",)
    FILEFORMAT_FONT_WOFF = ("font/woff",)
    FILEFORMAT_FONT_WOFF2 = ("font/woff2",)
    FILEFORMAT_IMAGE_BMP = ("image/bmp",)
    FILEFORMAT_IMAGE_CGM = ("image/cgm",)
    FILEFORMAT_IMAGE_DICOM_RLE = ("image/dicom-rle",)
    FILEFORMAT_IMAGE_EMF = ("image/emf",)
    FILEFORMAT_IMAGE_EXAMPLE = ("image/example",)
    FILEFORMAT_IMAGE_FITS = ("image/fits",)
    FILEFORMAT_IMAGE_G3FAX = ("image/g3fax",)
    FILEFORMAT_IMAGE_GIF = ("image/gif",)
    FILEFORMAT_IMAGE_IEF = ("image/ief",)
    FILEFORMAT_IMAGE_JLS = ("image/jls",)
    FILEFORMAT_IMAGE_JP2 = ("image/jp2",)
    FILEFORMAT_IMAGE_JPEG = ("image/jpeg",)
    FILEFORMAT_IMAGE_JPM = ("image/jpm",)
    FILEFORMAT_IMAGE_JPX = ("image/jpx",)
    FILEFORMAT_IMAGE_KTX = ("image/ktx",)
    FILEFORMAT_IMAGE_NAPLPS = ("image/naplps",)
    FILEFORMAT_IMAGE_PNG = ("image/png",)
    FILEFORMAT_IMAGE_PRS_BTIF = ("image/prs.btif",)
    FILEFORMAT_IMAGE_PRS_PTI = ("image/prs.pti",)
    FILEFORMAT_IMAGE_PWG_RASTER = ("image/pwg-raster",)
    FILEFORMAT_IMAGE_SVG_XML = ("image/svg+xml",)
    FILEFORMAT_IMAGE_T38 = ("image/t38",)
    FILEFORMAT_IMAGE_TIFF = ("image/tiff",)
    FILEFORMAT_IMAGE_TIFF_FX = ("image/tiff-fx",)
    FILEFORMAT_IMAGE_VND_ADOBE_PHOTOSHOP = ("image/vnd.adobe.photoshop",)
    FILEFORMAT_IMAGE_VND_AIRZIP_ACCELERATOR_AZV = ("image/vnd.airzip.accelerator.azv",)
    FILEFORMAT_IMAGE_VND_CNS_INF2 = ("image/vnd.cns.inf2",)
    FILEFORMAT_IMAGE_VND_DECE_GRAPHIC = ("image/vnd.dece.graphic",)
    FILEFORMAT_IMAGE_VND_DJVU = ("image/vnd.djvu",)
    FILEFORMAT_IMAGE_VND_DWG = ("image/vnd.dwg",)
    FILEFORMAT_IMAGE_VND_DXF = ("image/vnd.dxf",)
    FILEFORMAT_IMAGE_VND_DVB_SUBTITLE = ("image/vnd.dvb.subtitle",)
    FILEFORMAT_IMAGE_VND_FASTBIDSHEET = ("image/vnd.fastbidsheet",)
    FILEFORMAT_IMAGE_VND_FPX = ("image/vnd.fpx",)
    FILEFORMAT_IMAGE_VND_FST = ("image/vnd.fst",)
    FILEFORMAT_IMAGE_VND_FUJIXEROX_EDMICS_MMR = ("image/vnd.fujixerox.edmics-mmr",)
    FILEFORMAT_IMAGE_VND_FUJIXEROX_EDMICS_RLC = ("image/vnd.fujixerox.edmics-rlc",)
    FILEFORMAT_IMAGE_VND_GLOBALGRAPHICS_PGB = ("image/vnd.globalgraphics.pgb",)
    FILEFORMAT_IMAGE_VND_MICROSOFT_ICON = ("image/vnd.microsoft.icon",)
    FILEFORMAT_IMAGE_VND_MIX = ("image/vnd.mix",)
    FILEFORMAT_IMAGE_VND_MS_MODI = ("image/vnd.ms-modi",)
    FILEFORMAT_IMAGE_VND_MOZILLA_APNG = ("image/vnd.mozilla.apng",)
    FILEFORMAT_IMAGE_VND_NET_FPX = ("image/vnd.net-fpx",)
    FILEFORMAT_IMAGE_VND_RADIANCE = ("image/vnd.radiance",)
    FILEFORMAT_IMAGE_VND_SEALED_PNG = ("image/vnd.sealed.png",)
    FILEFORMAT_IMAGE_VND_SEALEDMEDIA_SOFTSEAL_GIF = (
        "image/vnd.sealedmedia.softseal.gif",
    )
    FILEFORMAT_IMAGE_VND_SEALEDMEDIA_SOFTSEAL_JPG = (
        "image/vnd.sealedmedia.softseal.jpg",
    )
    FILEFORMAT_IMAGE_VND_SVF = ("image/vnd.svf",)
    FILEFORMAT_IMAGE_VND_TENCENT_TAP = ("image/vnd.tencent.tap",)
    FILEFORMAT_IMAGE_VND_VALVE_SOURCE_TEXTURE = ("image/vnd.valve.source.texture",)
    FILEFORMAT_IMAGE_VND_WAP_WBMP = ("image/vnd.wap.wbmp",)
    FILEFORMAT_IMAGE_VND_XIFF = ("image/vnd.xiff",)
    FILEFORMAT_IMAGE_VND_ZBRUSH_PCX = ("image/vnd.zbrush.pcx",)
    FILEFORMAT_IMAGE_WMF = ("image/wmf",)
    FILEFORMAT_IMAGE_X_EMF = ("image/x-emf",)
    FILEFORMAT_IMAGE_X_WMF = ("image/x-wmf",)
    FILEFORMAT_MESSAGE_CPIM = ("message/CPIM",)
    FILEFORMAT_MESSAGE_DELIVERY_STATUS = ("message/delivery-status",)
    FILEFORMAT_MESSAGE_DISPOSITION_NOTIFICATION = ("message/disposition-notification",)
    FILEFORMAT_MESSAGE_EXAMPLE = ("message/example",)
    FILEFORMAT_MESSAGE_EXTERNAL_BODY = ("message/external-body",)
    FILEFORMAT_MESSAGE_FEEDBACK_REPORT = ("message/feedback-report",)
    FILEFORMAT_MESSAGE_GLOBAL = ("message/global",)
    FILEFORMAT_MESSAGE_GLOBAL_DELIVERY_STATUS = ("message/global-delivery-status",)
    FILEFORMAT_MESSAGE_GLOBAL_DISPOSITION_NOTIFICATION = (
        "message/global-disposition-notification",
    )
    FILEFORMAT_MESSAGE_GLOBAL_HEADERS = ("message/global-headers",)
    FILEFORMAT_MESSAGE_HTTP = ("message/http",)
    FILEFORMAT_MESSAGE_IMDN_XML = ("message/imdn+xml",)
    FILEFORMAT_MESSAGE_NEWS = ("message/news",)
    FILEFORMAT_MESSAGE_PARTIAL = ("message/partial",)
    FILEFORMAT_MESSAGE_RFC822 = ("message/rfc822",)
    FILEFORMAT_MESSAGE_S_HTTP = ("message/s-http",)
    FILEFORMAT_MESSAGE_SIP = ("message/sip",)
    FILEFORMAT_MESSAGE_SIPFRAG = ("message/sipfrag",)
    FILEFORMAT_MESSAGE_TRACKING_STATUS = ("message/tracking-status",)
    FILEFORMAT_MESSAGE_VND_SI_SIMP = ("message/vnd.si.simp",)
    FILEFORMAT_MESSAGE_VND_WFA_WSC = ("message/vnd.wfa.wsc",)
    FILEFORMAT_MODEL_3MF = ("model/3mf",)
    FILEFORMAT_MODEL_EXAMPLE = ("model/example",)
    FILEFORMAT_MODEL_GLTF_JSON = ("model/gltf+json",)
    FILEFORMAT_MODEL_IGES = ("model/iges",)
    FILEFORMAT_MODEL_MESH = ("model/mesh",)
    FILEFORMAT_MODEL_VND_COLLADA_XML = ("model/vnd.collada+xml",)
    FILEFORMAT_MODEL_VND_DWF = ("model/vnd.dwf",)
    FILEFORMAT_MODEL_VND_FLATLAND_3DML = ("model/vnd.flatland.3dml",)
    FILEFORMAT_MODEL_VND_GDL = ("model/vnd.gdl",)
    FILEFORMAT_MODEL_VND_GS_GDL = ("model/vnd.gs-gdl",)
    FILEFORMAT_MODEL_VND_GTW = ("model/vnd.gtw",)
    FILEFORMAT_MODEL_VND_MOML_XML = ("model/vnd.moml+xml",)
    FILEFORMAT_MODEL_VND_MTS = ("model/vnd.mts",)
    FILEFORMAT_MODEL_VND_OPENGEX = ("model/vnd.opengex",)
    FILEFORMAT_MODEL_VND_PARASOLID_TRANSMIT_BINARY = (
        "model/vnd.parasolid.transmit.binary",
    )
    FILEFORMAT_MODEL_VND_PARASOLID_TRANSMIT_TEXT = (
        "model/vnd.parasolid.transmit.text",
    )
    FILEFORMAT_MODEL_VND_ROSETTE_ANNOTATED_DATA_MODEL = (
        "model/vnd.rosette.annotated-data-model",
    )
    FILEFORMAT_MODEL_VND_VALVE_SOURCE_COMPILED_MAP = (
        "model/vnd.valve.source.compiled-map",
    )
    FILEFORMAT_MODEL_VND_VTU = ("model/vnd.vtu",)
    FILEFORMAT_MODEL_VRML = ("model/vrml",)
    FILEFORMAT_MODEL_X3D_VRML = ("model/x3d-vrml",)
    FILEFORMAT_MODEL_X3D_FASTINFOSET = ("model/x3d+fastinfoset",)
    FILEFORMAT_MODEL_X3D_XML = ("model/x3d+xml",)
    FILEFORMAT_MULTIPART_ALTERNATIVE = ("multipart/alternative",)
    FILEFORMAT_MULTIPART_APPLEDOUBLE = ("multipart/appledouble",)
    FILEFORMAT_MULTIPART_BYTERANGES = ("multipart/byteranges",)
    FILEFORMAT_MULTIPART_DIGEST = ("multipart/digest",)
    FILEFORMAT_MULTIPART_ENCRYPTED = ("multipart/encrypted",)
    FILEFORMAT_MULTIPART_EXAMPLE = ("multipart/example",)
    FILEFORMAT_MULTIPART_FORM_DATA = ("multipart/form-data",)
    FILEFORMAT_MULTIPART_HEADER_SET = ("multipart/header-set",)
    FILEFORMAT_MULTIPART_MIXED = ("multipart/mixed",)
    FILEFORMAT_MULTIPART_PARALLEL = ("multipart/parallel",)
    FILEFORMAT_MULTIPART_RELATED = ("multipart/related",)
    FILEFORMAT_MULTIPART_REPORT = ("multipart/report",)
    FILEFORMAT_MULTIPART_SIGNED = ("multipart/signed",)
    FILEFORMAT_MULTIPART_VND_BINT_MED_PLUS = ("multipart/vnd.bint.med-plus",)
    FILEFORMAT_MULTIPART_VOICE_MESSAGE = ("multipart/voice-message",)
    FILEFORMAT_MULTIPART_X_MIXED_REPLACE = ("multipart/x-mixed-replace",)
    FILEFORMAT_TEXT_1D_INTERLEAVED_PARITYFEC = ("text/1d-interleaved-parityfec",)
    FILEFORMAT_TEXT_CACHE_MANIFEST = ("text/cache-manifest",)
    FILEFORMAT_TEXT_CALENDAR = ("text/calendar",)
    FILEFORMAT_TEXT_CSS = ("text/css",)
    FILEFORMAT_TEXT_CSV = ("text/csv",)
    FILEFORMAT_TEXT_CSV_SCHEMA = ("text/csv-schema",)
    FILEFORMAT_TEXT_DIRECTORY = ("text/directory",)
    FILEFORMAT_TEXT_DNS = ("text/dns",)
    FILEFORMAT_TEXT_ECMASCRIPT = ("text/ecmascript",)
    FILEFORMAT_TEXT_ENCAPRTP = ("text/encaprtp",)
    FILEFORMAT_TEXT_ENRICHED = ("text/enriched",)
    FILEFORMAT_TEXT_EXAMPLE = ("text/example",)
    FILEFORMAT_TEXT_FWDRED = ("text/fwdred",)
    FILEFORMAT_TEXT_GRAMMAR_REF_LIST = ("text/grammar-ref-list",)
    FILEFORMAT_TEXT_HTML = ("text/html",)
    FILEFORMAT_TEXT_JAVASCRIPT = ("text/javascript",)
    FILEFORMAT_TEXT_JCRCND = ("text/jcr-cnd",)
    FILEFORMAT_TEXT_MARKDOWN = ("text/markdown",)
    FILEFORMAT_TEXT_MIZAR = ("text/mizar",)
    FILEFORMAT_TEXT_N3 = ("text/n3",)
    FILEFORMAT_TEXT_PARAMETERS = ("text/parameters",)
    FILEFORMAT_TEXT_PARITYFEC = ("text/parityfec",)
    FILEFORMAT_TEXT_PLAIN = ("text/plain",)
    FILEFORMAT_TEXT_PROVENANCE_NOTATION = ("text/provenance-notation",)
    FILEFORMAT_TEXT_PRS_FALLENSTEIN_RST = ("text/prs.fallenstein.rst",)
    FILEFORMAT_TEXT_PRS_LINES_TAG = ("text/prs.lines.tag",)
    FILEFORMAT_TEXT_PRS_PROP_LOGIC = ("text/prs.prop.logic",)
    FILEFORMAT_TEXT_RAPTORFEC = ("text/raptorfec",)
    FILEFORMAT_TEXT_RED = ("text/RED",)
    FILEFORMAT_TEXT_RFC822_HEADERS = ("text/rfc822-headers",)
    FILEFORMAT_TEXT_RICHTEXT = ("text/richtext",)
    FILEFORMAT_TEXT_RTF = ("text/rtf",)
    FILEFORMAT_TEXT_RTP_ENC_AESCM128 = ("text/rtp-enc-aescm128",)
    FILEFORMAT_TEXT_RTPLOOPBACK = ("text/rtploopback",)
    FILEFORMAT_TEXT_RTX = ("text/rtx",)
    FILEFORMAT_TEXT_SGML = ("text/sgml",)
    FILEFORMAT_TEXT_STRINGS = ("text/strings",)
    FILEFORMAT_TEXT_T140 = ("text/t140",)
    FILEFORMAT_TEXT_TAB_SEPARATED_VALUES = ("text/tab-separated-values",)
    FILEFORMAT_TEXT_TROFF = ("text/troff",)
    FILEFORMAT_TEXT_TURTLE = ("text/turtle",)
    FILEFORMAT_TEXT_ULPFEC = ("text/ulpfec",)
    FILEFORMAT_TEXT_URI_LIST = ("text/uri-list",)
    FILEFORMAT_TEXT_VCARD = ("text/vcard",)
    FILEFORMAT_TEXT_VND_A = ("text/vnd.a",)
    FILEFORMAT_TEXT_VND_ABC = ("text/vnd.abc",)
    FILEFORMAT_TEXT_VND_ASCII_ART = ("text/vnd.ascii-art",)
    FILEFORMAT_TEXT_VND_CURL = ("text/vnd.curl",)
    FILEFORMAT_TEXT_VND_DEBIAN_COPYRIGHT = ("text/vnd.debian.copyright",)
    FILEFORMAT_TEXT_VND_DMCLIENTSCRIPT = ("text/vnd.DMClientScript",)
    FILEFORMAT_TEXT_VND_DVB_SUBTITLE = ("text/vnd.dvb.subtitle",)
    FILEFORMAT_TEXT_VND_ESMERTEC_THEME_DESCRIPTOR = (
        "text/vnd.esmertec.theme-descriptor",
    )
    FILEFORMAT_TEXT_VND_FLY = ("text/vnd.fly",)
    FILEFORMAT_TEXT_VND_FMI_FLEXSTOR = ("text/vnd.fmi.flexstor",)
    FILEFORMAT_TEXT_VND_GRAPHVIZ = ("text/vnd.graphviz",)
    FILEFORMAT_TEXT_VND_IN3D_3DML = ("text/vnd.in3d.3dml",)
    FILEFORMAT_TEXT_VND_IN3D_SPOT = ("text/vnd.in3d.spot",)
    FILEFORMAT_TEXT_VND_IPTC_NEWSML = ("text/vnd.IPTC.NewsML",)
    FILEFORMAT_TEXT_VND_IPTC_NITF = ("text/vnd.IPTC.NITF",)
    FILEFORMAT_TEXT_VND_LATEX_Z = ("text/vnd.latex-z",)
    FILEFORMAT_TEXT_VND_MOTOROLA_REFLEX = ("text/vnd.motorola.reflex",)
    FILEFORMAT_TEXT_VND_MS_MEDIAPACKAGE = ("text/vnd.ms-mediapackage",)
    FILEFORMAT_TEXT_VND_NET2PHONE_COMMCENTER_COMMAND = (
        "text/vnd.net2phone.commcenter.command",
    )
    FILEFORMAT_TEXT_VND_RADISYS_MSML_BASIC_LAYOUT = (
        "text/vnd.radisys.msml-basic-layout",
    )
    FILEFORMAT_TEXT_VND_SI_URICATALOGUE = ("text/vnd.si.uricatalogue",)
    FILEFORMAT_TEXT_VND_SUN_J2ME_APP_DESCRIPTOR = ("text/vnd.sun.j2me.app-descriptor",)
    FILEFORMAT_TEXT_VND_TROLLTECH_LINGUIST = ("text/vnd.trolltech.linguist",)
    FILEFORMAT_TEXT_VND_WAP_SI = ("text/vnd.wap.si",)
    FILEFORMAT_TEXT_VND_WAP_SL = ("text/vnd.wap.sl",)
    FILEFORMAT_TEXT_VND_WAP_WML = ("text/vnd.wap.wml",)
    FILEFORMAT_TEXT_VND_WAP_WMLSCRIPT = ("text/vnd.wap.wmlscript",)
    FILEFORMAT_TEXT_XML = ("text/xml",)
    FILEFORMAT_TEXT_XML_EXTERNAL_PARSED_ENTITY = ("text/xml-external-parsed-entity",)
    FILEFORMAT_VIDEO_1D_INTERLEAVED_PARITYFEC = ("video/1d-interleaved-parityfec",)
    FILEFORMAT_VIDEO_3GPP = ("video/3gpp",)
    FILEFORMAT_VIDEO_3GPP2 = ("video/3gpp2",)
    FILEFORMAT_VIDEO_3GPP_TT = ("video/3gpp-tt",)
    FILEFORMAT_VIDEO_BMPEG = ("video/BMPEG",)
    FILEFORMAT_VIDEO_BT656 = ("video/BT656",)
    FILEFORMAT_VIDEO_CELB = ("video/CelB",)
    FILEFORMAT_VIDEO_DV = ("video/DV",)
    FILEFORMAT_VIDEO_ENCAPRTP = ("video/encaprtp",)
    FILEFORMAT_VIDEO_EXAMPLE = ("video/example",)
    FILEFORMAT_VIDEO_H261 = ("video/H261",)
    FILEFORMAT_VIDEO_H263 = ("video/H263",)
    FILEFORMAT_VIDEO_H263_1998 = ("video/H263-1998",)
    FILEFORMAT_VIDEO_H263_2000 = ("video/H263-2000",)
    FILEFORMAT_VIDEO_H264 = ("video/H264",)
    FILEFORMAT_VIDEO_H264_RCDO = ("video/H264-RCDO",)
    FILEFORMAT_VIDEO_H264_SVC = ("video/H264-SVC",)
    FILEFORMAT_VIDEO_H265 = ("video/H265",)
    FILEFORMAT_VIDEO_ISO_SEGMENT = ("video/iso.segment",)
    FILEFORMAT_VIDEO_JPEG = ("video/JPEG",)
    FILEFORMAT_VIDEO_JPEG2000 = ("video/jpeg2000",)
    FILEFORMAT_VIDEO_MJ2 = ("video/mj2",)
    FILEFORMAT_VIDEO_MP1S = ("video/MP1S",)
    FILEFORMAT_VIDEO_MP2P = ("video/MP2P",)
    FILEFORMAT_VIDEO_MP2T = ("video/MP2T",)
    FILEFORMAT_VIDEO_MP4 = ("video/mp4",)
    FILEFORMAT_VIDEO_MP4V_ES = ("video/MP4V-ES",)
    FILEFORMAT_VIDEO_MPV = ("video/MPV",)
    FILEFORMAT_VIDEO_MPEG = ("video/mpeg",)
    FILEFORMAT_VIDEO_MPEG4_GENERIC = ("video/mpeg4-generic",)
    FILEFORMAT_VIDEO_NV = ("video/nv",)
    FILEFORMAT_VIDEO_OGG = ("video/ogg",)
    FILEFORMAT_VIDEO_PARITYFEC = ("video/parityfec",)
    FILEFORMAT_VIDEO_POINTER = ("video/pointer",)
    FILEFORMAT_VIDEO_QUICKTIME = ("video/quicktime",)
    FILEFORMAT_VIDEO_RAPTORFEC = ("video/raptorfec",)
    FILEFORMAT_VIDEO_RAW = ("video/raw",)
    FILEFORMAT_VIDEO_RTP_ENC_AESCM128 = ("video/rtp-enc-aescm128",)
    FILEFORMAT_VIDEO_RTPLOOPBACK = ("video/rtploopback",)
    FILEFORMAT_VIDEO_RTX = ("video/rtx",)
    FILEFORMAT_VIDEO_SMPTE292M = ("video/SMPTE292M",)
    FILEFORMAT_VIDEO_ULPFEC = ("video/ulpfec",)
    FILEFORMAT_VIDEO_VC1 = ("video/vc1",)
    FILEFORMAT_VIDEO_VND_CCTV = ("video/vnd.CCTV",)
    FILEFORMAT_VIDEO_VND_DECE_HD = ("video/vnd.dece.hd",)
    FILEFORMAT_VIDEO_VND_DECE_MOBILE = ("video/vnd.dece.mobile",)
    FILEFORMAT_VIDEO_VND_DECE_MP4 = ("video/vnd.dece.mp4",)
    FILEFORMAT_VIDEO_VND_DECE_PD = ("video/vnd.dece.pd",)
    FILEFORMAT_VIDEO_VND_DECE_SD = ("video/vnd.dece.sd",)
    FILEFORMAT_VIDEO_VND_DECE_VIDEO = ("video/vnd.dece.video",)
    FILEFORMAT_VIDEO_VND_DIRECTV_MPEG = ("video/vnd.directv.mpeg",)
    FILEFORMAT_VIDEO_VND_DIRECTV_MPEG_TTS = ("video/vnd.directv.mpeg-tts",)
    FILEFORMAT_VIDEO_VND_DLNA_MPEG_TTS = ("video/vnd.dlna.mpeg-tts",)
    FILEFORMAT_VIDEO_VND_DVB_FILE = ("video/vnd.dvb.file",)
    FILEFORMAT_VIDEO_VND_FVT = ("video/vnd.fvt",)
    FILEFORMAT_VIDEO_VND_HNS_VIDEO = ("video/vnd.hns.video",)
    FILEFORMAT_VIDEO_VND_IPTVFORUM_1DPARITYFEC_1010 = (
        "video/vnd.iptvforum.1dparityfec-1010",
    )
    FILEFORMAT_VIDEO_VND_IPTVFORUM_1DPARITYFEC_2005 = (
        "video/vnd.iptvforum.1dparityfec-2005",
    )
    FILEFORMAT_VIDEO_VND_IPTVFORUM_2DPARITYFEC_1010 = (
        "video/vnd.iptvforum.2dparityfec-1010",
    )
    FILEFORMAT_VIDEO_VND_IPTVFORUM_2DPARITYFEC_2005 = (
        "video/vnd.iptvforum.2dparityfec-2005",
    )
    FILEFORMAT_VIDEO_VND_IPTVFORUM_TTSAVC = ("video/vnd.iptvforum.ttsavc",)
    FILEFORMAT_VIDEO_VND_IPTVFORUM_TTSMPEG2 = ("video/vnd.iptvforum.ttsmpeg2",)
    FILEFORMAT_VIDEO_VND_MOTOROLA_VIDEO = ("video/vnd.motorola.video",)
    FILEFORMAT_VIDEO_VND_MOTOROLA_VIDEOP = ("video/vnd.motorola.videop",)
    FILEFORMAT_VIDEO_VND_MPEGURL = ("video/vnd.mpegurl",)
    FILEFORMAT_VIDEO_VND_MS_PLAYREADY_MEDIA_PYV = ("video/vnd.ms-playready.media.pyv",)
    FILEFORMAT_VIDEO_VND_NOKIA_INTERLEAVED_MULTIMEDIA = (
        "video/vnd.nokia.interleaved-multimedia",
    )
    FILEFORMAT_VIDEO_VND_NOKIA_VIDEOVOIP = ("video/vnd.nokia.videovoip",)
    FILEFORMAT_VIDEO_VND_OBJECTVIDEO = ("video/vnd.objectvideo",)
    FILEFORMAT_VIDEO_VND_RADGAMETTOOLS_BINK = ("video/vnd.radgamettools.bink",)
    FILEFORMAT_VIDEO_VND_RADGAMETTOOLS_SMACKER = ("video/vnd.radgamettools.smacker",)
    FILEFORMAT_VIDEO_VND_SEALED_MPEG1 = ("video/vnd.sealed.mpeg1",)
    FILEFORMAT_VIDEO_VND_SEALED_MPEG4 = ("video/vnd.sealed.mpeg4",)
    FILEFORMAT_VIDEO_VND_SEALED_SWF = ("video/vnd.sealed.swf",)
    FILEFORMAT_VIDEO_VND_SEALEDMEDIA_SOFTSEAL_MOV = (
        "video/vnd.sealedmedia.softseal.mov",
    )
    FILEFORMAT_VIDEO_VND_UVVU_MP4 = ("video/vnd.uvvu.mp4",)
    FILEFORMAT_VIDEO_VND_VIVO = ("video/vnd.vivo",)
    FILEFORMAT_VIDEO_VP8 = ("video/VP8",)
