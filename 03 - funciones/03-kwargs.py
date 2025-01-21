def get_product(**datos):  # kwargs = key word arguments
    print(datos["id"], datos["name"])


get_product(id="23",
            name="iPhone",
            desc="Smartphone")
