import pyttsx3,PyPDF2

#insert name of your pdf 
pdfreader = PyPDF2.PdfFileReader(open('Lorem_ipsum.pdf', 'rb'))
speaker = pyttsx3.init()

for page_num in range(pdfreader.numPages):
    text = pdfreader.getPage(page_num).extractText()
    finalText = text.strip().replace('\n', ' ')
    print(finalText)

#name mp3 file whatever you would like
speaker.save_to_file(finalText, "lorem.mp3")
speaker.runAndWait()

speaker.stop()

#MP3 FILE IS NOT SAVING YET!