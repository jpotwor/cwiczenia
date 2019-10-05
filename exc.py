import pandas
import numpy


df = pandas.DataFrame({
    'one': pandas.Series(numpy.random.randn(3)),
})

print(df)


