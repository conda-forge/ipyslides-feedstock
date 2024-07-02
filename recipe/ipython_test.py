try:
    import ipyslides
except RuntimeError as e:
    if str(e) == "Not in a Notebook!":
        pass
