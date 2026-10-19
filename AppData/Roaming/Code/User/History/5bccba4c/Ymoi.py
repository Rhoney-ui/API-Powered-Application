// Demo key: no account required.
const response = await fetch(
  'https://api.restcountries.com/countries/v5/names.common/Canada',
  { headers: { 'Authorization': 'Bearer rc_live_demo' } }
);
const data = await response.json();