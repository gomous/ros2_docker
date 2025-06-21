FROM osrf/ros:jazzy-desktop-full

SHELL ["/bin/bash", "-c"]

WORKDIR /app

COPY src ws_pub_sub/src

RUN cd ws_pub_sub/src && \
    source /opt/ros/jazzy/setup.bash && \
    colcon build

COPY entrypoint.sh /

ENTRYPOINT ["/entrypoint.sh"]

CMD ["bash"]



