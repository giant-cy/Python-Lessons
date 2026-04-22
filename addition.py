"""THIS IS ADDITION MODULE"""


int_1 = "1234323434343343443"
int_2 = "322323239234"



# ===================
#               73677
int_1 = "43993"
int_2 = "994"


# =====
# 44987

# initil i=1
#
# 1. i = 1, c=0
# 2. if i < L1, d1 = num1[L1-i], else 0
# 3. if i < L2, d2 = num2[L2-i], else 0
# 4. add d1 + d2 + c
# 5. c = sum / 10
# 6 ouput = (sum mod 10) + output
# 5. i ++


def addition_func(a, b):
    c = 0
    output = ""
    len_a = len(a) # 5
    len_b = len(b) # 3
    max_length = max(len_a, len_b)
    for i in range(1, max_length+1):
        if i <= len_a:
            d1 = a[len_a - i]
        else:
            d1 = 0
        if i <= len_b:
            d2 = b[len_b - i]
        else:
            d2 = 0
        sum = int(d1) + int(d2) + c
        c = sum // 10
        output = str(sum % 10) + output
    print(output)



print(__name__)

if __name__ == "__main__":
    addition_func("43993", "994")
    addition_func("3434", "3434")