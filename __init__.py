# coding=utf-8
from __future__ import absolute_import
from asyncio.windows_events import ERROR_CONNECTION_ABORTED
import serial

import octoprint.plugin

class Int(octoprint.plugin.StartupPlugin,
                       octoprint.plugin.TemplatePlugin,
                       octoprint.plugin.SettingsPlugin,
                       octoprint.plugin.AssetPlugin, octoprint.plugin.SettingsPlugin):
	def on_after_startup(self):
		self._logger.info("Hello World! (more: %s)" % self._settings.get(["url"]))
		try:
			nano_port = serial.Serial(dict.serial_port_nano, dict.serial_port_baud_rate, dict.serial_port_timeout)
		except:
			self._logger.exception("incorrect port, no MCU here")
		baud_check = ser.readline()
		if baud_check != dict.serial_port_baud_rate:
			self._logger.exception("baud rate doesn't match")

	def get_settings_defaults(self):
		return dict(
			url="https://en.wikipedia.org/wiki/Hello_world",
			tare=-10000,
			spool_weight=200,
			serial_port="/dev/ttyUSB0",
			serial_port_baud_rate=9600,
			serial_port_timeout=1
		)

	def get_template_configs(self):
		return [
			dict(type="navbar", custom_bindings=False),
			dict(type="settings", custom_bindings=False)
		]

	def get_assets(self):
		return dict(
			js=["js/helloworld.js"],
			css=["css/helloworld.css"],
			less=["less/helloworld.less"]
		)

__plugin_name__ = "Nano Filament Weight Sensor"
__plugin_pythoncompat__ = ">=3.8,>=0"
__plugin_implementation__ = Int()
