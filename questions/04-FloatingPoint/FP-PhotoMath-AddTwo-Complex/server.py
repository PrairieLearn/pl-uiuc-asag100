import random
def generate(data):
    exponent_1 = random.randint(0, 3)
    exponent_2 = random.randint(0, 3)

    exponent_a = max(exponent_1, exponent_2)
    exponent_b = min(exponent_1, exponent_2)

    mantissa_a = random.randint(0, 63)
    mantissa_b = random.randint(0, 63)

    a = (1 + (mantissa_a / 64)) * (2**exponent_a)
    b = (1 + (mantissa_b / 64)) * (2**exponent_b)

    data["params"]["a"] = a
    data["params"]["b"] = b
    data["params"]["arep"] = f"1.{bin(mantissa_a)[2:].zfill(6)} \\times 2^{exponent_a}"
    data["params"]["brep"] = f"1.{bin(mantissa_b)[2:].zfill(6)} \\times 2^{exponent_b}"

    mantissa_sum = mantissa_a + ((64 + mantissa_b) >> (exponent_a - exponent_b))
    exponent_sum = exponent_a
    if mantissa_sum >= 64:
        mantissa_sum = (mantissa_sum - 64) >> 1
        exponent_sum += 1

    data["params"]["sumrep"] = f"1.{bin(mantissa_sum)[2:].zfill(6)} \\times 2^{exponent_sum}"
    data["params"]["sumdec"] = ((1 + (mantissa_sum)/64) * (2 ** exponent_sum))
    data["params"]["sumerr"] = round(abs(a + b - ((1 + (mantissa_sum)/64) * (2 ** exponent_sum))) / (a + b), 6)

    if exponent_sum > 3 or data["params"]["sumerr"] == 0:
        # regenerate
        return generate(data)
