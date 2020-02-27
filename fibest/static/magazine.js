tinymce.init({

    selector: 'textarea',
    menubar: "",

    plugins: [
        'advlist autolink autoresize lists link  charmap preview',
        'searchreplace ',
        '  paste help wordcount table'
    ],
    toolbar: ' undo redo paste searchreplace | fontsizeselect backcolor forecolor | ' +
        ' bold italic  underline  | alignleft aligncenter ' +
        ' alignright alignjustify | bullist numlist outdent indent table|' +
        ' removeformat | help',
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

    max_chars: 1500, // max. allowed chars
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
        ed.on('init', function (args) {
            editor_id = args.target.id;
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


