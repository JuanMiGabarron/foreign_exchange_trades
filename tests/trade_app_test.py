import time
import unittest

from selenium import webdriver


class TradesTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_trades_app(self):
        # Lets check our main page
        self.browser.get('http://localhost:8000')

        # Check the title if the web is the correct
        self.assertIn('trades', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h4').text
        self.assertIn('Booked Trades', header_text)

        # Check if the list is generated in the table
        table_body = self.browser.find_element_by_tag_name('tbody')
        self.assertTrue(table_body, True)

        # We see the trades! Now lets go and create one
        # first look for the button to create a new trade
        new_trade = self.browser.find_element_by_link_text('New Trade')
        self.assertTrue(new_trade, True)

        # Look at this! We found it camon click it!
        new_trade.click()

        time.sleep(2)

        # It seems that the web has changed, lets check the header
        header_text = self.browser.find_element_by_tag_name('h4').text
        self.assertIn('New Trade', header_text)

        # Nice! we are in the correct page
        # Select EUR for the sell currency
        sell_select = self.browser.find_element_by_id('sell_currency')
        for option in sell_select.find_elements_by_tag_name('option'):
            if option.text == 'EUR':
                option.click()
                break
        self.assertTrue('EUR', sell_select.text)

        # Take a break we are calling the api
        time.sleep(1)

        # Now lets put some coins in the sell amount, at least 10!
        sell_input = self.browser.find_element_by_id('sell_amount')
        sell_input.send_keys('10')
        self.assertTrue(sell_input.get_attribute('value'), '10')

        # Perfect! Now we want to buy USD, select it!
        buy_select = self.browser.find_element_by_id('buy_currency')
        for option in buy_select.find_elements_by_tag_name('option'):
            if option.text == 'USD':
                option.click()
                break
        self.assertTrue('USD', buy_select.text)

        # We can see the rate and the money we are going to buy now, right?
        rate = self.browser.find_element_by_id('current_rate').text
        self.assertTrue(rate, True)

        buy_input = self.browser.find_element_by_id(
            'buy_amount'
        ).get_attribute('value')
        self.assertTrue(buy_input, True)

        # Are the amount correct?
        amount = float(sell_input.get_attribute('value')) * float(rate)
        self.assertTrue("%.2f" % amount, buy_input)

        # Awesome! Lets create it
        self.browser.find_element_by_id('create_trade').click()

        # Wait! Api crossing
        time.sleep(1)

        success = self.browser.find_element_by_css_selector(
            '.alert-success'
        )
        self.assertTrue('Trade created', success.text)

        # WoW! We made it! Lets cancel and see the list in the main page!
        self.browser.find_element_by_link_text('Cancel').click()

        time.sleep(1)

        table = self.browser.find_element_by_id('trade_table')
        self.assertIn('EUR 10.00 USD', table.text)

        # Cool! Now we can save our wallet we finish!

if __name__ == '__main__':
    unittest.main(warnings='ignore')
