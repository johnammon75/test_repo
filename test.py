from Frappe import frappe
import PyC
import rConfig

rConfig.get()
frappe.use()

s = PyC.Py_SetPath()
