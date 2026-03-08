exports.handler = async (event) => {
  if (event.httpMethod !== 'POST') {
    return { statusCode: 405, body: 'Method Not Allowed' }
  }

  const { email } = JSON.parse(event.body)

  if (!email || !email.includes('@')) {
    return { statusCode: 400, body: JSON.stringify({ message: 'Invalid email' }) }
  }

  const response = await fetch('https://api.brevo.com/v3/contacts', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'api-key': process.env.BREVO_API_KEY
    },
    body: JSON.stringify({
      email: email,
      listIds: [3],
      updateEnabled: true
    })
  })

  if (response.ok || response.status === 204) {
    return { statusCode: 200, body: JSON.stringify({ message: 'success' }) }
  } else {
    return { statusCode: 400, body: JSON.stringify({ message: 'error' }) }
  }
}