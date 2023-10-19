from main.config.industries import IndustryConfig
from main.config.variables import industry_config
from main.industry import Industry
from main.location.location import Location


class TestIndustries:

    def test_create_industry(self):

        test_location = Location(name='test_location', map_url='test_map_url')
        test_industry = Industry(name='test_industry',location=test_location, config=IndustryConfig(**industry_config['sawmill']))
        assert  test_industry.name == 'test_industry'
        assert  test_industry.location.name == 'test_location'
        assert  test_industry.location.map_url == 'test_map_url'
        assert  test_industry.config.input_1 == 'log'
        assert  test_industry.config.stock_input_1 == 0
        assert  test_industry.config.max_store_input_1 == 1000
        assert  test_industry.load_input('log', 100) == 100
        assert  test_industry.unload_input('log', 100) == 0
