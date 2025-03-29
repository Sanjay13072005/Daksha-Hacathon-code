require.config({ paths: { vs: 'https://cdnjs.cloudflare.com/ajax/libs/monaco-editor/0.34.1/min/vs' } });

require(['vs/editor/editor.main'], function () {
    monaco.editor.create(document.getElementById('editor'), {
        value: '// Write your code here...',
        language: 'javascript',
        theme: 'vs-dark',
        fontSize: 16,
        automaticLayout: true
    });
});
