const API_BASE = '';

async function api(path, options = {}) {
  const res = await fetch(`${API_BASE}${path}`, {
    headers: { 'Content-Type': 'application/json', ...options.headers },
    ...options,
  });
  if (!res.ok) {
    const body = await res.json().catch(() => ({}));
    throw new Error(body.detail || `Error ${res.status}`);
  }
  if (res.status === 204) return null;
  return res.json();
}

async function loadData() {
  try {
    const data = await api('/api/data?limit=20');
    const tbody = document.getElementById('data-tbody');
    if (data.length === 0) {
      tbody.innerHTML = '<tr><td colspan="6" class="empty">⌀ No hay datos en la red</td></tr>';
      return;
    }
    tbody.innerHTML = data.map(item => `
      <tr>
        <td title="${item.id}">${item.id.slice(0, 8)}…</td>
        <td>${item.handle}</td>
        <td>${escapeHtml(item.content).slice(0, 40)}${item.content.length > 40 ? '…' : ''}</td>
        <td>${item.source || '—'}</td>
        <td title="${item.hash}">${item.hash.slice(0, 8)}…</td>
        <td><button class="btn-small" data-id="${item.id}">[ ELIMINAR ]</button></td>
      </tr>
    `).join('');

    tbody.querySelectorAll('.btn-small').forEach(btn => {
      btn.addEventListener('click', () => deleteData(btn.dataset.id));
    });
  } catch (err) {
    document.getElementById('data-tbody').innerHTML =
      `<tr><td colspan="6" class="empty" style="color:#ff0040">⚠ ${err.message}</td></tr>`;
  }
}

async function loadStats() {
  try {
    const stats = await api('/api/stats');
    document.getElementById('stat-total').textContent = stats.total;
    const top = stats.top_handles?.[0];
    document.getElementById('stat-top').textContent = top ? `${top.handle} (${top.count})` : '—';
  } catch {
    // silent
  }
}

async function deleteData(id) {
  try {
    await api(`/api/data/${id}`, { method: 'DELETE' });
    await Promise.all([loadData(), loadStats()]);
  } catch (err) {
    alert(`Error: ${err.message}`);
  }
}

document.getElementById('data-form').addEventListener('submit', async (e) => {
  e.preventDefault();
  const content = document.getElementById('content').value.trim();
  const source = document.getElementById('source').value.trim() || null;
  const msgEl = document.getElementById('form-msg');

  if (!content) {
    msgEl.textContent = '⚠ El contenido es obligatorio.';
    msgEl.className = 'msg error';
    return;
  }

  try {
    await api('/api/data', {
      method: 'POST',
      body: JSON.stringify({ content, source }),
    });
    document.getElementById('content').value = '';
    document.getElementById('source').value = '';
    msgEl.textContent = '✅ Dato transmitido exitosamente.';
    msgEl.className = 'msg success';
    await Promise.all([loadData(), loadStats()]);
  } catch (err) {
    msgEl.textContent = `⚠ ${err.message}`;
    msgEl.className = 'msg error';
  }
});

function escapeHtml(str) {
  const div = document.createElement('div');
  div.textContent = str;
  return div.innerHTML;
}

loadData();
loadStats();
