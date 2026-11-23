import tkinter as tk

# Data functions
def convert():
    try:
        far = float(farEntry.get())
        result.set(f"{far} in Centigrade is {((far - 32) * 5 /9):.2f}")
        return True
    except ValueError:
        result.set('Input error...Plesae enter valid numbers')

def clear():
    farEntry.delete(0, tk.END)
    result.set('Awaiting input...')

# GUI
window = tk.Tk()

window.title("Farenheit to Centigrade")

farLabel = tk.Label(
    window,
    text='Farenheit'
)

farLabel.grid(row=0, column=0)

farEntry = tk.Entry(window)
farEntry.grid(row=0, column=1)

convertBtn = tk.Button(window, text="Convert", command=convert)
convertBtn.grid(row=1, column=1)

clearBtn = tk.Button(window, text="Clear", command=clear)
clearBtn.grid(row=1, column=0)

result = tk.StringVar(value='Awaiting input...')
resultLabel = tk.Label(window, textvariable=result)
resultLabel.grid(row=3, column=1)

window.geometry("400x300")

window.mainloop()
