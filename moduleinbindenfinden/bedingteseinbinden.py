try:
    import mod2
    mod2.fkt1()
except ImportError:
    print("Fehler beim Einbinden")
    import uv.mod2
    uv.mod2.fkt1()
