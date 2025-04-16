senhat = input("crie uma senha que SÓ TENHA NUMEROS:")
while senhat.isdigit() is False:
    senhat = input ("tente novamente:")
    if senhat.isdigit() is True :
        print ("senha criada")
        break