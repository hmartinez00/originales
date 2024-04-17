El archivo `credentials.json` debe contener las credenciales de la cuenta de servicio de Google Cloud que se utiliza para acceder a la API de Google Sheets. Debe tener el siguiente formato:

```json
{
  "type": "service_account",
  "project_id": "PROJECT_ID",
  "private_key_id": "PRIVATE_KEY_ID",
  "private_key": "-----BEGIN PRIVATE KEY-----\nYOUR_PRIVATE_KEY\n-----END PRIVATE KEY-----\n",
  "client_email": "CLIENT_EMAIL",
  "client_id": "CLIENT_ID",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/PROJECT_ID%40PROJECT_NUMBER.iam.gserviceaccount.com"
}
```

Debes reemplazar los siguientes valores de marcador de posición con la información correspondiente de tu cuenta de servicio:

* **PROJECT_ID**: El ID del proyecto de Google Cloud asociado con tu cuenta de servicio.
* **PRIVATE_KEY_ID**: El ID de la clave privada asociada con tu cuenta de servicio.
* **PRIVATE_KEY**: La clave privada en formato PEM.
* **CLIENT_EMAIL**: La dirección de correo electrónico de la cuenta de servicio.
* **CLIENT_ID**: El ID de cliente de la cuenta de servicio.