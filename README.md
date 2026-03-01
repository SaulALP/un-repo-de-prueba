## Integración con n8n (OpenHands / automatización)

Este repositorio puede integrarse con un flujo n8n que automatiza la creación/actualización de archivos mediante el agente OpenHands.

### Archivo de workflow
El workflow utilizado (JSON para importar en n8n) contiene un Webhook que recibe prompts y ejecuta: petición a un agente Django, invocación de OpenHands y validaciones posteriores. Importa el JSON en n8n para reproducir el flujo.

> Nota: el archivo del workflow fue provisto por el autor y referencia endpoints externos; antes de importar, revisa y sustituye las URLs y credenciales por tus valores seguros.

### Requisitos / credenciales en n8n
- `Header Auth` para la API de OpenHands / All-Hands (token en header).
- `GitHub OAuth` (opcional) para leer/escribir en repositorios privados.
- (Opcional) Credencial para Google/PaLM si se usa un nodo para evaluación (Gemini).

### Cómo probar localmente
1. Importa el workflow en n8n.
2. Configura credenciales.
3. Activa el workflow.
4. Llama al webhook con JSON:
```json
{
  "prompt": "Crea el archivo Python michi.py en el repositorio. El código debe ser el juego michi. Al finalizar, imprime todo el código generado aquí en el chat y haz git push a la rama main."
}
