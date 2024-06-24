from Frappe import frappe
import PyC
import rConfig

rConfig.get()
frappe.use()

s = PyC.Py_SetPath()
import langchain_experimental 

langchain_experimental.use(xx, y)
