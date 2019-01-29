from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Production"),
			"icon": "fa fa-star",
			"items": [
				{
					"type": "doctype",
					"name": "Work Order",
					"description": _("Orders released for production."),
				},
				{
					"type": "doctype",
					"name": "Production Plan",
					"description": _("Generate Material Requests (MRP) and Work Orders."),
				},
				{
					"type": "doctype",
					"name": "Stock Entry",
				},
				{
					"type": "doctype",
					"name": "Timesheet",
					"description": _("Time Sheet for manufacturing."),
				},

			]
		},
		{
			"label": _("Bill of Materials"),
			"items": [
				{
					"type": "doctype",
					"name": "BOM",
					"description": _("Bill of Materials (BOM)"),
					"label": _("Bill of Materials")
				},
				{
					"type": "doctype",
					"name": "BOM",
					"icon": "fa fa-sitemap",
					"label": _("BOM Browser"),
					"description": _("Tree of Bill of Materials"),
					"link": "Tree/BOM",
				},
				{
					"type": "doctype",
					"name": "Item",
					"description": _("All Products or Services."),
				},
				{
					"type": "doctype",
					"name": "Workstation",
					"description": _("Where manufacturing operations are carried."),
				},
				{
					"type": "doctype",
					"name": "Operation",
					"description": _("Details of the operations carried out."),
				},

			]
		},
		{
			"label": _("Tools"),
			"icon": "fa fa-wrench",
			"items": [
				{
					"type": "doctype",
					"name": "BOM Update Tool",
					"description": _("Replace BOM and update latest price in all BOMs"),
				},
			]
		},
		{
			"label": _("Setup"),
			"items": [
				{
					"type": "doctype",
					"name": "Manufacturing Settings",
					"description": _("Global settings for all manufacturing processes."),
				}
			]
		},
		{
			"label": _("Reports"),
			"icon": "fa fa-list",
			"items": [
				{
					"type": "report",
					"is_query_report": True,
					"name": "Open Work Orders",
					"doctype": "Work Order"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Work Orders in Progress",
					"doctype": "Work Order"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Issued Items Against Work Order",
					"doctype": "Work Order"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Completed Work Orders",
					"doctype": "Work Order"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Production Analytics",
					"doctype": "Work Order"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "BOM Search",
					"doctype": "BOM"
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "BOM Stock Report",
					"doctype": "BOM"
				}
			]
		},
		{
			"label": _("Help"),
			"icon": "fa fa-facetime-video",
			"items": [
				{
					"type": "help",
					"label": _("Bill of Materials"),
					"youtube_id": "hDV0c1OeWLo"
				},
				{
					"type": "help",
					"label": _("Work Order"),
					"youtube_id": "ZotgLyp2YFY"
				},
			]
		}
	]
