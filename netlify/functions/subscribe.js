exports.handler = async (event) => {
  if (event.httpMethod !== 'POST') {
    return { statusCode: 405, body: 'Method Not Allowed' }
  }

  let parsed
  try {
    parsed = JSON.parse(event.body)
  } catch {
    return { statusCode: 400, body: JSON.stringify({ message: 'Invalid request' }) }
  }

  const email = (parsed.email || '').trim().toLowerCase()
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
  if (!emailRegex.test(email)) {
    return { statusCode: 400, body: JSON.stringify({ message: 'Invalid email' }) }
  }

  try {
    const response = await fetch('https://api.brevo.com/v3/contacts', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'api-key': process.env.BREVO_API_KEY
      },
      body: JSON.stringify({
        email,
        listIds: [3],
        updateEnabled: true
      })
    })

    if (response.ok || response.status === 204) {
      return { statusCode: 200, body: JSON.stringify({ message: 'success' }) }
    } else {
      const body = await response.text()
      console.error('Brevo API error:', response.status, body)
      return { statusCode: 400, body: JSON.stringify({ message: 'error' }) }
    }
  } catch (error) {
    console.error('Newsletter subscription failed:', error)
    return { statusCode: 500, body: JSON.stringify({ message: 'server error' }) }
  }
}
