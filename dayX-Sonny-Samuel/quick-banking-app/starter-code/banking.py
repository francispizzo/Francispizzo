#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Replace "pass" with your code

class BankAccount(object):
    def __init__(acc, label, balance):
        acc.label = label
        acc.balance = balance
    def __str__(acc):
        return "> %s %s." % (acc.balance, acc.label)
    def withdraw(acc, withdraw):
        if acc.withdraw <= acc.balance:
            acc.balance = acc.balance - acc.withdraw
        else:
           acc.withdraw > acc.balance
