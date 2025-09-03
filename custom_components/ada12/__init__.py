from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

DOMAIN = "ada12"

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Set up Ada12 from a config entry."""
    await hass.config_entries.async_forward_entry_setups(entry, ["sensor"])
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry):
    """Unload Ada12 config entry."""
    return await hass.config_entries.async_unload_platforms(entry, ["sensor"])
