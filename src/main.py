from gui import App, MainFrame


if __name__ == "__main__":
    app = App()

    main = MainFrame(app)
    main.grid()

    app.mainloop()
