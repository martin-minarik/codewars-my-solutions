from string import ascii_lowercase

def solve(st, k):
    st = list(st)
    for char in ascii_lowercase:
        for i in range(k):
            try:
                st.pop(st.index(char))
                k -= 1
                if k == 0: 
                    raise ValueError
                    
            except ValueError:
                break
                
        if k == 0: 
            break
    
    return "".join(st)
    