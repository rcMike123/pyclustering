"""!

@brief Unit-test runner for containers.

@authors Andrei Novikov (pyclustering@yandex.ru)
@date 2014-2019
@copyright GNU Public License

@cond GNU_PUBLIC_LICENSE
    PyClustering is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    
    PyClustering is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.
    
    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
@endcond

"""


import unittest;
from pyclustering.tests.suite_holder import suite_holder;

from pyclustering.container.tests.unit          import container_unit_tests;


class container_tests(suite_holder):
    def __init__(self):
        super().__init__();
        container_unit_tests.fill_suite(self.get_suite());

    @staticmethod
    def fill_suite(container_suite):
        container_unit_tests.fill_suite(container_suite);


if __name__ == "__main__":
    container_tests().run();