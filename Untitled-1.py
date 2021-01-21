with open ('input.txt' , 'r') as f:
    x=list(eval(f.readline()))
with open ('output.txt' , 'w') as f:
    f.write(str(x))
    y=sorted(str(x))
    f.write(str(y))
    x.sort(reverse=True)
    f.write(str(x))
    f.write(str(len(x)))
    f.write(str(max(x)))
    f.write(str(min(x)))
    x.extend([111])
    f.write(str(x))
    x[1]=222
    f.write(str(x))