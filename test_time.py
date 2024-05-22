from datetime import datetime, timedelta

nowe = datetime.now()
then = datetime(2024, 5, 1)
secs = 1716383597.369032
print((nowe - then).total_seconds())
print(then + timedelta(0, secs))
