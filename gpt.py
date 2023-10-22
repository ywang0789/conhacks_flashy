import openai 
import api_keys as keys
import PyPDF2

MODEL = "gpt-3.5-turbo"

class gpt:
    def __init__(self, key):
        self.key = key
        openai.api_key = self.key
        self.history = []
        self.history.append(
            {
                "role": "system",
                "content": "Your goal is to turn this set of notes into 5 flash cards while following these formatting instructions. Title: The note should have a relevent title. Subject: The note should have a relevent subject. Question: Question from the content to ask the user. Answer: Answer from the content relevent to the asked question." ,
            }
        )

    def chat(self, user_input):
        self.history.append({"role": "user", "content": user_input})
        response = openai.ChatCompletion.create(model=MODEL, messages=self.history, max_tokens=500)

        response = response["choices"][0]["message"]["content"]

        self.history.append({"role": "system", "content": response})
        return response


class PDFtoFlashcards:
    def __init__(self, fileName):
        self.pdfFileName = fileName
    
    def convertToNote(fileName):
        pdfFileObj = open(fileName, 'rb')

        pdfReader = PyPDF2.PdfReader(pdfFileObj)

        numPages = len(pdfReader.pages)
        count = 0
        output = ""

        while count < numPages:
            pageObj = pdfReader.pages[count]
            count += 1
            b = gpt(keys.gpt_api_key)
            output += (b.chat(pageObj.extract_text()))

        pdfFileObj.close()

        flashcards = []

        for x in range(5):
            new_flashcard = Flashcard()
            new_flashcard.question = b.chat("Based on the information provided above, make one flashcard question")
            new_flashcard.answer = b.chat("Make 1 flashcard answer based on the above using content from the pdf:")
            flashcards.append(new_flashcard)  # Append the new flashcard to the list

        return flashcards

class Flashcard:
     def init(self):
        self.question = ''
        self.answer = ''


if __name__ == "__main__":
    output = PDFtoFlashcards.convertToNote("ProjectPlanGroup3.pdf")

    for x in output:
        print(x.question)
        print(x.answer)
    
    print(type(output))

        


