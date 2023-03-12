import uuid

def generate_gifcard():

    gifcard = uuid.uuid4()

    gifcard = str(gifcard).replace('-', '')

    gifcard = str(gifcard)[0:4].upper() + '-' + str(gifcard)[4:8].upper() + '-' + str(gifcard)[8:12].upper()

    return gifcard