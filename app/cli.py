import click
import captcha_extractor
from tqdm import trange
from time import sleep


@click.command()
@click.option("--iterations", default=10 , help="Numbers of iteration to check captcha solver")
def check_captcha_solver(iterations):
    """Program that resolves captchas with pytesseract ocr and selenium"""
    for test in trange(iterations):
        captcha_extractor.extract()


if __name__ == "__main__":
    check_captcha_solver()
