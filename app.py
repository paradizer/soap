"""local SOAP server"""
from spyne import Application, rpc, ServiceBase, Unicode
from spyne.protocol.soap import Soap11
# from spyne.protocol.json import JsonDocument
from spyne.server.wsgi import WsgiApplication
from lxml import etree
from yandex_translate import YandexTranslate
from config import API_KEY


class Soap(ServiceBase):
    """Class for Soap"""
    @rpc(Unicode, _returns=Unicode)
    def insoap(ctx, words):
        """Method to be called remoutly"""
        print(etree.tostring(ctx.in_document))
        translate = YandexTranslate(API_KEY)
        transl = translate.translate(words, 'en')
        tr_answer = transl['text'][0]
        return tr_answer


APP = Application([Soap], tns='Translator', in_protocol=Soap11(validator='lxml'),
                  out_protocol=Soap11())
# APP = Application([Soap], tns='Translator', in_protocol=JsonDocument(validator='soft'),
#                   out_protocol=JsonDocument())
APPLICATION = WsgiApplication(APP)


if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    SERVER = make_server('0.0.0.0', 8000, APPLICATION)
    SERVER.serve_forever()
