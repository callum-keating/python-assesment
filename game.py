try:
    from rich.console import Console
    from rich.table import Table
except ImportError:
    print("ERROR: couldn't run due to missing dependency. Please run pip install rich")
    quit()
except Exception as e:
    print("ERROR: an unknown error occured message: ", e)
    quit()
finally:
    try:
        import readchar
    except ImportError:
        print("ERROR: couldn't run due to missing dependency. Please run pip install readchar")
        quit()
    except Exception as e:
        print("ERROR: an unknown error occured message: ", e)
        quit()



def mainMenu():
    console = Console()
    console.set_alt_screen(True)
    console.show_cursor(False)
    console.clear()  # Clear screen at the start of each loop
    console.print("[center underline large]press p/q")
    menu = Table(title="Main Menu")
    menu.add_column("Options", justify="center")
    menu.add_row("P: Play")
    menu.add_row("Q: Quit")

    console.print(menu)

    key = readchar.readchar()
    key = key.lower()
    if key == "p":
        console.print("[green]Starting game...[/green]")
    elif key == "q":
        console.print("[red]Quitting...[/red]")
def end():
    console = Console()
    console.show_cursor(True)
    console.set_alt_screen(False)

mainMenu()
end()