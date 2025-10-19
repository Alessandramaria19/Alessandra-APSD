# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import string
    x="Potrivit ABC Science, la apus și la răsărit calea parcursă de razele solare prin atmosferă este cea mai lungă. Prin urmare, culorile care reușesc să ajungă mai ușor la noi sunt roșul și portocaliul, în timp ce albastrul și violetul se pierd din cauza difuziei."
    lung=len(x)
    mj=lung//2
    jum1=x[:mj]
    jum2=x[mj:]
    jum1=jum1.upper()
    jum1=jum1.strip()
    jum2=jum2[::-1]
    jum2=jum2.capitalize()
    set= str.maketrans('' ,'', string.punctuation)
    jum2=jum2.translate(set)
    print(jum1+jum2)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
