
import fire

def hello(name='world'):
    return f"Hello {name}"

if __name__ == '__main__':
    fire.Fire(hello)
