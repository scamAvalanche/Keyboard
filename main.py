import keyboard
import time

def write_with_delay(text, delay_seconds):
   for char in text:
       keyboard.write(char)
       time.sleep(delay_seconds / len(text))

def main():
   time.sleep(5)
   text = "since to under thing which will that mean tell hand one very still out those time by of nation general at go each possible mate keep down call line be over  this new do about good another only after long well use number more now there because and can problem think other so old also great but whem he or place a from such would should up right many child know if set course same state world around early for way not could system on year own while write little life face turn all begin as you school run large late person increase ask who most  against give part no any it consider hold high here man program the form"
   write_with_delay(text, 54)

if __name__ == "__main__":
   main()
