// Animated pytest-style test runner panel
const body    = document.getElementById('tr-body');
const summary = document.getElementById('tr-summary');
const bar     = document.getElementById('tr-progress');
const pct     = document.getElementById('tr-pct');

if (!body) throw new Error('no tr-body');

// Test cases drawn from the actual resume content
const TESTS = [
  { id: 'test_session_init',                  suite: 'core',       result: 'pass', ms: 12  },
  { id: 'test_selenium_framework_scalability', suite: 'automation', result: 'pass', ms: 340 },
  { id: 'test_mainframe_module_parity[001]',   suite: 'migration',  result: 'pass', ms: 88  },
  { id: 'test_mainframe_module_parity[002]',   suite: 'migration',  result: 'pass', ms: 92  },
  { id: 'test_mainframe_module_parity[003]',   suite: 'migration',  result: 'pass', ms: 78  },
  { id: 'test_api_ingestion_workflow',          suite: 'api',        result: 'pass', ms: 201 },
  { id: 'test_rest_endpoint_response_codes',   suite: 'api',        result: 'pass', ms: 156 },
  { id: 'test_db_verification_sql_query',      suite: 'api',        result: 'pass', ms: 44  },
  { id: 'test_concurrent_users[50_sessions]',  suite: 'load',       result: 'pass', ms: 620 },
  { id: 'test_edge_case_network_timeout',      suite: 'load',       result: 'warn', ms: 410 },
  { id: 'test_rbac_access_control',            suite: 'security',   result: 'pass', ms: 95  },
  { id: 'test_pub_sub_latency',               suite: 'integration', result: 'pass', ms: 188 },
  { id: 'test_email_sync_delta',              suite: 'integration', result: 'pass', ms: 233 },
  { id: 'test_nlp_query_handling',            suite: 'ai',          result: 'warn', ms: 501 },
  { id: 'test_production_rca_isolation',      suite: 'stability',   result: 'pass', ms: 67  },
  { id: 'test_regression_zero_defects',       suite: 'regression',  result: 'pass', ms: 310 },
  { id: 'test_sensor_detection_accuracy',     suite: 'iot',         result: 'pass', ms: 145 },
  { id: 'test_gsm_alert_latency_5s',          suite: 'iot',         result: 'pass', ms: 220 },
  { id: 'test_coverage_threshold[95pct]',     suite: 'coverage',    result: 'pass', ms: 18  },
  { id: 'test_full_suite_complete',           suite: 'core',        result: 'pass', ms: 8   },
];

function printLine(html, delay) {
  return new Promise(resolve => {
    setTimeout(() => {
      const div = document.createElement('div');
      div.className = 'tr-line';
      div.innerHTML = html;
      body.appendChild(div);
      body.scrollTop = body.scrollHeight;
      resolve();
    }, delay);
  });
}

async function runTests() {
  let elapsed = 0;

  await printLine(`<span class="tr-dim">platform linux -- Python 3.12.0, pytest-8.3.2, Selenium 4.25</span>`, elapsed);
  elapsed += 120;
  await printLine(`<span class="tr-head">collecting ... ${TESTS.length} items</span>`, elapsed);
  elapsed += 200;
  await printLine(`<span class="tr-dim">━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ test session starts ━━━</span>`, elapsed);
  elapsed += 100;

  let passed = 0, warned = 0, failed = 0;

  for (let i = 0; i < TESTS.length; i++) {
    const test = TESTS[i];
    elapsed += 80 + test.ms * 0.6;

    const progress = Math.round(((i + 1) / TESTS.length) * 100);
    bar.style.width = progress + '%';
    pct.textContent = progress + '%';

    let icon, cls, label;
    if (test.result === 'pass') { icon = 'PASSED'; cls = 'tr-pass'; passed++; }
    else if (test.result === 'warn') { icon = 'WARNED'; cls = 'tr-warn'; warned++; }
    else { icon = 'FAILED'; cls = 'tr-fail'; failed++; }

    await printLine(
      `<span class="${cls}">${icon.padEnd(6)}</span> <span class="tr-dim">${test.suite}/</span><span class="tr-info">${test.id}</span> <span class="tr-dim">${test.ms}ms</span>`,
      elapsed
    );

    // Update live summary
    summary.innerHTML =
      `<span style="color:var(--pass)">${passed} passed</span>` +
      (warned ? ` <span style="color:var(--warn)">· ${warned} warned</span>` : '') +
      (failed ? ` <span style="color:var(--fail)">· ${failed} failed</span>` : '');
  }

  elapsed += 200;
  const total_ms = TESTS.reduce((a, t) => a + t.ms, 0);
  await printLine(`<span class="tr-dim">━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</span>`, elapsed);
  elapsed += 60;
  await printLine(
    `<span class="tr-pass">✓ ${passed} passed</span>` +
    (warned ? ` <span class="tr-warn">⚠ ${warned} warnings</span>` : '') +
    ` <span class="tr-dim">in ${(total_ms / 1000).toFixed(2)}s</span>`,
    elapsed
  );

  // Loop — restart after a pause
  elapsed += 3000;
  setTimeout(() => {
    body.innerHTML = '';
    bar.style.width = '0%';
    pct.textContent = '0%';
    summary.textContent = 'Initializing...';
    runTests();
  }, elapsed);
}

// Respect reduced motion — show static summary instead
const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
if (prefersReducedMotion) {
  body.innerHTML = `<div class="tr-line"><span class="tr-pass">✓ ${TESTS.length} passed</span> <span class="tr-dim">in 3.73s</span></div>`;
  bar.style.width = '100%';
  pct.textContent = '100%';
  summary.innerHTML = `<span style="color:var(--pass)">${TESTS.length} passed</span>`;
} else {
  runTests();
}
