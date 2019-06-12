from rest_framework.views import APIView
from phishing_detection import scan
from rest_framework.response import Response
# Create your views here.
class prueba(APIView):


    def get(self, request):

        #nombre = self.request.GET['userid']
        #print("hola mi nombre es",nombre)
        #isM = scan.yaraScan(email="hola y adios")
        return Response({"Hola": "alejandro"})

    def post(self, request):
        """
        {   Ejemplo para probar peticion POST
            "asunto" : "premio",
            "cuerpo" : "Buenas tardes, ha resultado ganador de un premio valorado en 1000000 de euros, pincha aqui",
            "fecha" : "27/05/2019",
            "destinatarios" : "ale@hotmail.com, antonio@gmail.com, manuel@hotmail.es",
            "emisor" : "phishing@hotmail.com"
        }
        """
        #hacer json.loads(request) una vez se tenga la estructura definida, esto es solo para probar por ahora
        datos = self.request.data
        asunto = datos["asunto"]
        cuerpo = datos["cuerpo"]
        fecha = datos["fecha"]
        destinatarios = datos["destinatarios"]
        emisor = datos["emisor"]

        email = "From: "+emisor+"\n" \
                +"To: " + destinatarios + "\n" \
                +"Subject: "+asunto+"\n"\
                +cuerpo+"\n"\
                +"Date: "+fecha+"\n"


        print(email)  #Solo para ir probando. Quitar luego!!!


        matches = scan.yaraScan(email=email)   #Devuelve todas las reglas que han dado match al email

        isM = matches.__len__() != 0

        return Response({"isPS": isM ,"Reglas":matches})
