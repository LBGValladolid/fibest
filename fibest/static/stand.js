tinymce.PluginManager.add('PDF', function (editor, url) {
    // Add a button that opens a window
    editor.ui.registry.addButton('pdf', {
        text: 'pdf',
        onAction: function () {
            // Open window
            editor.windowManager.open({
                title: 'PDF Embed',
                body: {
                    type: 'panel',
                    items: [
                        {
                            type: 'input',
                            name: 'title',
                            label: 'PDF url'
                        }
                    ]
                },
                buttons: [
                    {
                        type: 'cancel',
                        text: 'Close'
                    },
                    {
                        type: 'submit',
                        text: 'Save',
                        primary: true
                    }
                ],

                onSubmit: function (api) {
                    // Insert content when the window form is submitted
                    editor.insertContent('<iframe  width="90%" height="500px" src="' + api.getData().title + '">');
                    api.close();
                }
            });
        }
    });
});

tinymce.init({
    selector: 'textarea',
    menubar: false,

    plugins: [
        'advlist autolink autoresize lists link image charmap preview',
        'searchreplace  ',
        'media table paste  help wordcount PDF'
    ],
    toolbar: ' undo redo paste searchreplace | fontsizeselect backcolor forecolor | ' +
        ' bold italic  underline  | alignleft aligncenter ' +
        ' alignright alignjustify | bullist numlist outdent indent |' +
        ' removeformat | pdf image media | table | help',
    content_css: [
        '//fonts.googleapis.com/css?family=Lato:300,300i,400,400i',
        '//www.tiny.cloud/css/codepen.min.css'
    ],
    contextmenu: 'false',
    min_height: 500,
    max_height: 800,
    branding: false,
    help_tabs: [
        'shortcuts',
        'keyboardnav'],
    extended_valid_elements: [ "iframe[src|frameborder|style|scrolling|class|width|height|name|align]"],

    max_chars: 500, // max. allowed chars
    setup: function (ed) {
        ed.on('keydown', function (e) {
            var wordcount = tinymce.activeEditor.plugins.wordcount;
            var inp = String.fromCharCode(event.keyCode);
            if (!(/[a-zA-Z0-9-_ ]/.test(inp))) return true;

            if (wordcount.body.getCharacterCount() > this.settings.max_chars) {
                e.preventDefault();
                e.stopPropagation();
                return false;
            }
            return true;
        });
    },
    paste_preprocess: function (plugin, args) {
        var editor = tinymce.get(tinymce.activeEditor.id);
        var len = editor.contentDocument.body.innerText.length;
        var text = $(args.content).text();
        if (len + text.length > editor.settings.max_chars) {
            alert('Pasting this exceeds the maximum allowed number of ' + editor.settings.max_chars + ' characters.');
            args.content = '';
        }
    }
});

