import PySimpleGUI as sg

library= ["The Alchemist", "1984", "Animal Farm", "Legend", "Harry Potter", "Rich Dad Poor Dad"]
lend = ["This Book", "That Book", "No more than this book", "The Hand-maid Tale"]

lever = True

# Borrow function
def bo(k):
  global library, lend
  try:
    n = library.index(k)
  except:
    s = 'The book is not in the library'
    b = 'Continue'
  else:
    s = 'The book is available for lending'
    b = 'Borrow'
  finally:
    f = [ [sg.T(library)],
          [sg.T(s)],
          [sg.B(b)]]
  w = sg.Window("D's library",f)
  event,values = w.read(close=True)
  if event == "Borrow":
    lend.append(k)
    lend.sort()
    library.remove(k)
    library.sort()

# Return function
def re(k):
  global lend, library
  try:
    n = lend.index(k)
  except:
    s = "The book is not currently on lend, please enter the correct name"
    b = "Continue"
  else:
    s = "Thank you for returning the book"
    b = "Return"
  finally:
    f = [ [sg.T(lend)],
          [sg.T(s)],
          [sg.B(b)]]
  w = sg.Window("D's library",f)
  event,values = w.read(close = True)
  if event == "Return":
    library.append(k)
    library.sort()
    lend.remove(k)
    lend.sort()

# Last call function     
def ask():
  global lever
  f = [ [sg.T("Thank you for choosing our service")],
        [sg.T("Do you want to do anything else?")],
        [sg.B("Yes"),sg.B("No")]]
  w = sg.Window("D's library",f)
  event, values = w.read(close = True)
  if event == "No":
    lever = False

# Main prompt
def main():
  global lever
  sg.theme('DarkAmber')
  layout = [  [sg.T('What is the name of the book'), sg.In(key = "name")],
              [sg.B("Borrow")], [sg.B("Return")]]

  # Create the Window
  window = sg.Window("D's library", layout)

  # Event Loop to process "events" and get the "values" of the inputs
  event, values = window.read(close=True)
  if event == "Borrow":
    bo(values["name"])
    ask()
  elif event == "Return":
    re(values["name"])
    ask()
  elif event == sg.WIN_CLOSED:
    lever = False

# Main code
while lever:
  main()
