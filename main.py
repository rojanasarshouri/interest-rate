from interestrate import app , scrape_interest_rates

@app.route('/', methods=['GET'])
def scrape():
    scrape_interest_rates()
    return "Data scraped and stored in the database!"


if __name__ == '__main__':
    app.run(debug=True)