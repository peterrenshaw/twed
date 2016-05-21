import Html exposing (Html, Attribute, div, input, text)
import Html.App as Html
import Html.Events exposing (onClick, onInput)
import Html.Attributes exposing (..)
import String exposing (..)


-- #======
-- # name: form.elm
-- # date: 2016MAY21
-- #       2016MAY13
-- # prog: pr
-- # desc: builds simple form using basic function example
-- # vers: 0.17
-- # sorc: <http://guide.elm-lang.org/architecture/user_input/text_fields.html>
-- #       <http://elm-lang.org/examples/field>
-- #======


-- MAIN
main = 
    Html.beginnerProgram {model = model, 
                          view = view, 
                          update = update}


-- MODEL
type alias Model = 
    { content :  String
     , count : Int
    }

-- INIT
model : Model
model = 
    { content = ""
     , count = 0 }


-- UPDATE
type Msg
    = Change String


update : Msg -> Model -> Model
update msg model = 
    case msg of 
        Change newContent ->
            { model | content = newContent}


-- VIEW
view : Model -> Html Msg
view model =
    div []
        [ div [myStyle] [ messageCount model ]
        , input [ placeholder "", onInput Change, myStyle ] []
        , div [myStyle] [ text  (model.content) ]
        ]


-- FUNCS
messageCount : Model -> Html Msg
messageCount model = 
    let
        (size) =  String.length model.content
    in 
        div [] [text (toString size)]

-- STYLE
myStyle =
  style
    [ ("width", "100%")
    , ("height", "40px")
    , ("padding", "10px 0")
    , ("font-size", "2em")
    , ("text-align", "left")
    ]
