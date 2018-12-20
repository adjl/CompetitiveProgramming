#!/usr/bin/env python3

# LeetCode #690: Employee Importance
# https://leetcode.com/problems/employee-importance/description/

"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""


class Solution:
    def getImportance(self, employees, e_id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        e_table = {e.id: e for e in employees}
        return self._getImportance(e_table, e_id)

    def _getImportance(self, e_table, e_id):
        importance = e_table[e_id].importance
        for subordinate in e_table[e_id].subordinates:
            importance += self._getImportance(e_table, subordinate)
        return importance
