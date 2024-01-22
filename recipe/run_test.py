try:
    import ipyslides
except RuntimeException as e:
    if str(e) == "Not in a Notebook!":
        pass
