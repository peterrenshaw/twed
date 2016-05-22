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


import Html exposing (Html, Attribute, div, input, textarea, text)
import Html.App as Html
import Html.Events exposing (onClick, onInput)
import Html.Attributes exposing (..)
import String exposing (..)





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
        [ --div [myStyle] [ messageCount model ]
          inputCheck model          
        , div [myStyle] [textarea [ placeholder "", autofocus True, onInput Change,  myStyle] []]
        ]


-- FUNCS
messageCount : Model -> Html Msg
messageCount model = 
    let
        (size) =  140 - String.length model.content
    in 
        div [] [text (toString size)]

inputCheck : Model -> Html Msg
inputCheck model = 
    let 
        (color) =
            if String.length model.content < 140 then
                ("black")
            else
                ("red")
    in
         div [ style [("color", color)] ] [ messageCount model]

-- STYLE
myStyle =
  style
    [ ("width", "80%")
    , ("height", "60px")
    , ("font-size", "1em")
    , ("text-align", "left")
    ]

# vim: ff=unix:ts=4:sw=4:tw=78:noai:expandtab 
