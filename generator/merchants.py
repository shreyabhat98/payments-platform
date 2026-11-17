import csv
from faker import Faker

def make_merchant(fake, merchant_id):
    # return a dict: merchant_id, name, country, category
    return {
        "merchant_id": merchant_id,
        "name": fake.company(),
        "country": fake.country(),
        "category": fake.word()
    }

def main():
    fake = Faker()
    Faker.seed(42)
    # make 500 merchants and write them to data/merchants.csv
    merchants = [make_merchant(fake, i) for i in range(500)]
    with open("data/merchants.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["merchant_id", "name", "country", "category"])
        writer.writeheader()
        writer.writerows(merchants)

if __name__ == "__main__":
    main()