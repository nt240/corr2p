import click
import math
from scipy import stats

@click.command()
@click.option("--r", type=float, required=True)
@click.option("--n", type=int, required=True)
def main(r, n):
    t = r * math.sqrt((n - 2) / (1 - r * r))
    df = n - 2
    p = stats.t.sf(abs(t), df) * 2
    click.echo(f"r={r}, n={n}, t={t:.4f}, p={p:.6g}")

if __name__ == "__main__":
    main()