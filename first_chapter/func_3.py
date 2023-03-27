
import random
from typing import Any

def func_hard(a,b,c,d,*args,**kwargs:dict[Any,int]):
    if (args and kwargs) and (len(args)>1):
        return sum((a,b,c,d)) + sum(args[:2]) + random.choice(kwargs.values())
    else: return 0